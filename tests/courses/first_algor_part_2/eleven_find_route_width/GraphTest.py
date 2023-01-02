import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first_algor_part_2.eleven_find_route_width.Graph import SimpleGraph, Vertex


class GraphTest(unittest.TestCase):

    def addVertexes(self, graph, arr):
        for val in arr:
            graph.AddVertex(val)

    def test_find_through_near(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)

        result = graph.BreadthFirstSearch(1, 2)

        self.assertEqual(3, len(result))
        self.assertEqual(result[0].Value, 'B')
        self.assertEqual(result[1].Value, 'A')
        self.assertEqual(result[2].Value, 'C')

    def test_find_near(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)

        result = graph.BreadthFirstSearch(0, 1)

        self.assertEqual(2, len(result))
        self.assertEqual(result[0].Value, 'A')
        self.assertEqual(result[1].Value, 'B')

    def test_find_none_existing(self):
        graph = SimpleGraph(5)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)

        result = graph.BreadthFirstSearch(0, 4)

        self.assertEqual(0, len(result))