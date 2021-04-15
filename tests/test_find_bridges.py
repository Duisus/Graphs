import unittest

from algorithms.bridges import *
from graph_and_additional_classes import *


# https://www.geeksforgeeks.org/bridge-in-a-graph/
class BridgesFinderTests(unittest.TestCase):
    def test_find_on_simple_graph(self):
        graph = GraphBuilder() \
            .add_nodes(0, 1, 2, 3, 4) \
            .add_edges((1, 2), (1, 0), (0, 2), (0, 3), (3, 4)) \
            .build()

        actual = BridgesFinder().find(graph)

        self.assertCountEqual(
            {
                (graph[0], graph[3]),
                (graph[3], graph[4])
            },
            actual)

    def test_find_on_difficult_graph(self):
        graph = GraphBuilder() \
            .add_nodes(0, 1, 2, 3, 4, 5, 6) \
            .add_edges((0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (1, 6), (3, 5), (4, 5)) \
            .build()

        actual = BridgesFinder().find(graph)

        self.assertCountEqual(
            {(graph[1], graph[6])},
            actual)

    def test_find_on_chain(self):
        graph = GraphBuilder() \
            .add_nodes(0, 1, 2, 3) \
            .add_edges((0, 1), (1, 2), (2, 3)) \
            .build()

        actual = BridgesFinder().find(graph)

        self.assertCountEqual(
            {
                (graph[0], graph[1]),
                (graph[1], graph[2]),
                (graph[2], graph[3])
            },
            actual)
