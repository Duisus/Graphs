from collections import defaultdict

from graph_and_additional_classes import *


class BridgesFinder:
    def __init__(self):
        self.time = 0
        self.visited = defaultdict(lambda: False)
        self.up: Dict[Node, int] = {}
        self.tin: Dict[Node, int] = {}

    def _dfs(self, node: Node, parent: Node = None) -> Set[Node]:
        self.time += 1
        self.up[node] = self.tin[node] = self.time
        self.visited[node] = True
        bridges = set()

        for incident_node in node.children:
            if incident_node == parent:
                continue
            if self.visited[incident_node]:
                self.up[node] = min(self.up[node], self.tin[incident_node])
            else:
                bridges.update(self._dfs(incident_node, node))
                self.up[node] = min(self.up[node], self.up[incident_node])

                if self.up[incident_node] > self.tin[node]:
                    bridges.add((node, incident_node))

        return bridges

    def find(self, graph: Graph):
        bridges = set()

        for node in graph:
            if not self.visited[node]:
                bridges.update(self._dfs(node))

        return bridges


# https://e-maxx.ru/algo/bridge_searching
if __name__ == "__main__":
    graph = GraphBuilder() \
        .add_nodes(0, 1, 2, 3, 4) \
        .add_edges((1, 2), (1, 0), (0, 2), (0, 3), (3, 4)) \
        .build()

    print(BridgesFinder().find(graph))
