import unittest

from algorithms.articulation_points import *
from graph_and_additional_classes import *


# https://www.geeksforgeeks.org/articulation-points-or-cut-vertices-in-a-graph/
class ArticulationPointsFinderTests(unittest.TestCase):
    def test_find_on_simple_graph(self):
        graph = GraphBuilder() \
            .add_nodes(0, 1, 2, 3, 4) \
            .add_edges((1, 2), (1, 0), (0, 2), (0, 3), (3, 4)) \
            .build()

        actual = ArticulationPointsFinder().find(graph)

        self.assertEqual({graph[0], graph[3]}, actual)

    def test_find_on_difficult_graph(self):
        graph = GraphBuilder() \
            .add_nodes(0, 1, 2, 3, 4, 5, 6) \
            .add_edges((0, 1), (0, 2), (1, 2), (1, 3), (1, 4), (1, 6), (3, 5), (4, 5)) \
            .build()

        actual = ArticulationPointsFinder().find(graph)

        self.assertEqual({graph[1]}, actual)

    def test_find_on_chain(self):
        graph = GraphBuilder() \
            .add_nodes(0, 1, 2, 3) \
            .add_edges((0, 1), (1, 2), (2, 3)) \
            .build()

        actual = ArticulationPointsFinder().find(graph)

        self.assertEqual({graph[1], graph[2]}, actual)
