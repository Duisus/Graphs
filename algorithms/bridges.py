from graph_and_additional_classes import *
from . import dfs_finder


class BridgesFinder(dfs_finder.DfsFinder):
    def _get_updated_sought_entities(self, current_sought_entities, parent, current_node, next_node):
        if self.visited[next_node]:
            self.up[current_node] = min(self.up[current_node], self.tin[next_node])
        else:
            current_sought_entities += self._find_sought_entities_by_dfs(next_node, current_node)
            self.up[current_node] = min(self.up[current_node], self.up[next_node])

            if self.up[next_node] > self.tin[current_node]:
                current_sought_entities.append((current_node, next_node))

        return current_sought_entities


# https://e-maxx.ru/algo/bridge_searching
if __name__ == "__main__":
    graph = GraphBuilder() \
        .add_nodes(0, 1, 2, 3, 4) \
        .add_edges((1, 2), (1, 0), (0, 2), (0, 3), (3, 4)) \
        .build()

    print(BridgesFinder().find(graph))
