from typing import *


class Node:
    def __init__(self, num: int):
        self.num = num
        self._children = ()

    def add_children(self, *children: "Node"):
        self._children += children

    @property
    def children(self):
        return self._children

    def __repr__(self):
        return str(self.num)


class Graph:
    def __init__(self, nodes: Dict[int, Node]):
        self._nodes = nodes

    def __getitem__(self, item: int) -> Node:
        return self._nodes[item]

    def __iter__(self):
        return self._nodes.values().__iter__()


class GraphBuilder:
    _nodes: Dict[int, Node]

    def __init__(self):
        self._nodes = {}

    def add_nodes(self, *nodes_nums: int) -> "GraphBuilder":
        for num in nodes_nums:
            self._nodes[num] = Node(num)

        return self

    def add_edges(self, *edges: Tuple[int, int]) -> "GraphBuilder":
        """ Add unoriented edges """

        for edge in edges:
            first_node = self._nodes[edge[0]]
            second_node = self._nodes[edge[1]]
            first_node.add_children(second_node)
            second_node.add_children(first_node)

        return self

    def build(self) -> Graph:
        return Graph(self._nodes)

    # TODO add from_file
