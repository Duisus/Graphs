from graph_and_additional_classes import *
from . import dfs_finder


class ArticulationPointsFinder(dfs_finder.DfsFinder):
    def __init__(self):
        super().__init__()
        self.roots_children_count = 0

    def find(self, graph: Graph):
        return set(super().find(graph))

    def _find_sought_entities_by_dfs(self, node: Node, parent: Node = None):
        if parent is None:
            self.roots_children_count = 0

        result = super()._find_sought_entities_by_dfs(node, parent)

        if parent is None and self.roots_children_count >= 2:
            result.append(node)

        return result

    def _get_updated_sought_entities(
            self, current_sought_entities, parent, current_node, next_node):

        if self.visited[next_node]:
            self.up[current_node] = min(self.up[current_node], self.tin[next_node])
        else:
            current_sought_entities += self._find_sought_entities_by_dfs(next_node, current_node)
            self.up[current_node] = min(self.up[current_node], self.up[next_node])

            if parent is None:
                self.roots_children_count += 1
            elif self.up[next_node] >= self.tin[current_node]:
                current_sought_entities.append(current_node)

        return current_sought_entities


# https://e-maxx.ru/algo/cutpoints
# https://neerc.ifmo.ru/wiki/index.php?title=%D0%98%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BE%D0%B1%D1%85%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%B3%D0%BB%D1%83%D0%B1%D0%B8%D0%BD%D1%83_%D0%B4%D0%BB%D1%8F_%D0%BF%D0%BE%D0%B8%D1%81%D0%BA%D0%B0_%D1%82%D0%BE%D1%87%D0%B5%D0%BA_%D1%81%D0%BE%D1%87%D0%BB%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F
if __name__ == "__main__":
    graph = GraphBuilder() \
        .add_nodes(0, 1, 2, 3, 4) \
        .add_edges((1, 2), (1, 0), (0, 2), (0, 3), (3, 4)) \
        .build()

    print(ArticulationPointsFinder().find(graph))
