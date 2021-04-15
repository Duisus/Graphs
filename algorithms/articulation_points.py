from collections import defaultdict

from graph_and_additional_classes import *


class ArticulationPointsFinder:
    def __init__(self):
        self.time = 0
        self.visited = defaultdict(lambda: False)
        self.up: Dict[Node, int] = {}
        self.tin: Dict[Node, int] = {}

    def _dfs(self, node: Node, parent: Node = None) -> Set[Node]:
        self.time += 1
        self.up[node] = self.tin[node] = self.time
        self.visited[node] = True
        articulation_points = set()

        childerns_count = 0
        for incident_node in node.children:
            if incident_node == parent:
                continue
            if self.visited[incident_node]:
                self.up[node] = min(self.up[node], self.tin[incident_node])
            else:
                articulation_points.update(self._dfs(incident_node, node))
                childerns_count += 1
                self.up[node] = min(self.up[node], self.up[incident_node])

                if parent is not None and self.up[incident_node] >= self.tin[node]:
                    articulation_points.add(node)

        if parent is None and childerns_count >= 2:
            articulation_points.add(node)

        return articulation_points

    def find(self, graph: Graph):
        articulation_points = set()

        for node in graph:
            if not self.visited[node]:
                articulation_points.update(self._dfs(node))

        return articulation_points


# https://e-maxx.ru/algo/cutpoints
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D0%B1%D1%85%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%83_%D0%B4%D0%BB%D1%8F_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0_%D1%82%D0%BE%D1%87%D0%B5%D0%BA_%D1%81%D0%BE%D1%87%D0%BB%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F
if __name__ == "__main__":
    graph = GraphBuilder() \
        .add_nodes(0, 1, 2, 3, 4) \
        .add_edges((1, 2), (1, 0), (0, 2), (0, 3), (3, 4)) \
        .build()

    print(ArticulationPointsFinder().find(graph))
