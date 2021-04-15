from abc import ABC, abstractmethod
from collections import defaultdict

from graph_and_additional_classes import *


class DfsFinder(ABC):
    def __init__(self):
        self.time = 0
        self.visited = defaultdict(lambda: False)
        self.up: Dict[Node, int] = {}
        self.tin: Dict[Node, int] = {}

    def find(self, graph: Graph):
        sought_entities = []

        for node in graph:
            if not self.visited[node]:
                sought_entities += self._find_sought_entities_by_dfs(node)
        self._clear()

        return sought_entities

    def _find_sought_entities_by_dfs(self, node: Node, parent: Node = None) -> List[Node]:
        self.time += 1
        self.up[node] = self.tin[node] = self.time
        self.visited[node] = True
        sought_entities = []

        for incident_node in node.children:
            if incident_node == parent:
                continue
            else:
                sought_entities = self._get_updated_sought_entities(
                    sought_entities, parent, node, incident_node)

        return sought_entities

    def _clear(self):
        self.time = 0
        self.up.clear()
        self.tin.clear()
        self.visited.clear()

    @abstractmethod
    def _get_updated_sought_entities(
            self, current_sought_entities, parent, current_node, next_node):
        pass
