import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first_algor_part_2.eight_graph.Graph import SimpleGraph, Vertex


class GraphTest(unittest.TestCase):
    def test_add(self):
        graph = SimpleGraph(3)
        graph.AddVertex("A")
        self.assertEqual("A", graph.vertex[0].Value)
        self.assertIsNone(graph.vertex[1])
        self.assertIsNone(graph.vertex[2])
        graph.AddVertex("B")
        self.assertEqual("A", graph.vertex[0].Value)
        self.assertEqual("B", graph.vertex[1].Value)
        self.assertIsNone(graph.vertex[2])
        graph.AddVertex("C")
        self.assertEqual("A", graph.vertex[0].Value)
        self.assertEqual("B", graph.vertex[1].Value)
        self.assertEqual("C", graph.vertex[2].Value)

    def test_add_edge(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        self.assertEqual(1, graph.m_adjacency[0][1])
        self.assertEqual(1, graph.m_adjacency[1][0])
        self.assertEqual(0, graph.m_adjacency[0][2])
        self.assertEqual(0, graph.m_adjacency[2][0])
        self.assertEqual(0, graph.m_adjacency[1][2])
        self.assertEqual(0, graph.m_adjacency[2][1])

        graph.AddEdge(0, 2)
        self.assertEqual(1, graph.m_adjacency[0][1])
        self.assertEqual(1, graph.m_adjacency[1][0])
        self.assertEqual(1, graph.m_adjacency[0][2])
        self.assertEqual(1, graph.m_adjacency[2][0])
        self.assertEqual(0, graph.m_adjacency[1][2])
        self.assertEqual(0, graph.m_adjacency[2][1])

        graph.AddEdge(1, 2)
        self.assertEqual(1, graph.m_adjacency[0][1])
        self.assertEqual(1, graph.m_adjacency[1][0])
        self.assertEqual(1, graph.m_adjacency[0][2])
        self.assertEqual(1, graph.m_adjacency[2][0])
        self.assertEqual(1, graph.m_adjacency[1][2])
        self.assertEqual(1, graph.m_adjacency[2][1])

    def test_remove_edge(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        self.assertEqual(1, graph.m_adjacency[0][1])
        self.assertEqual(1, graph.m_adjacency[1][0])
        self.assertEqual(1, graph.m_adjacency[0][2])
        self.assertEqual(1, graph.m_adjacency[2][0])
        self.assertEqual(1, graph.m_adjacency[1][2])
        self.assertEqual(1, graph.m_adjacency[2][1])

        graph.RemoveEdge(0, 1)
        self.assertEqual(0, graph.m_adjacency[0][1])
        self.assertEqual(0, graph.m_adjacency[1][0])
        self.assertEqual(1, graph.m_adjacency[0][2])
        self.assertEqual(1, graph.m_adjacency[2][0])
        self.assertEqual(1, graph.m_adjacency[1][2])
        self.assertEqual(1, graph.m_adjacency[2][1])

        graph.RemoveEdge(0, 2)
        self.assertEqual(0, graph.m_adjacency[0][1])
        self.assertEqual(0, graph.m_adjacency[1][0])
        self.assertEqual(0, graph.m_adjacency[0][2])
        self.assertEqual(0, graph.m_adjacency[2][0])
        self.assertEqual(1, graph.m_adjacency[1][2])
        self.assertEqual(1, graph.m_adjacency[2][1])

        graph.RemoveEdge(1, 2)
        self.assertEqual(0, graph.m_adjacency[0][1])
        self.assertEqual(0, graph.m_adjacency[1][0])
        self.assertEqual(0, graph.m_adjacency[0][2])
        self.assertEqual(0, graph.m_adjacency[2][0])
        self.assertEqual(0, graph.m_adjacency[1][2])
        self.assertEqual(0, graph.m_adjacency[2][1])

    def test_is_edge(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(0, 2))

    def test_is_edge(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        graph.AddEdge(1, 2)

        self.assertTrue(graph.IsEdge(0, 1))
        self.assertTrue(graph.IsEdge(1, 2))
        self.assertFalse(graph.IsEdge(0, 2))

    def test_remove_vertex(self):
        graph = SimpleGraph(3)
        graph.AddVertex('A')
        graph.AddVertex('B')
        graph.AddVertex('C')
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        graph.RemoveVertex(0)
        self.assertIsNone(graph.vertex[0])
        self.assertEqual(0, graph.m_adjacency[0][1])
        self.assertEqual(0, graph.m_adjacency[1][0])
        self.assertEqual(0, graph.m_adjacency[0][2])
        self.assertEqual(0, graph.m_adjacency[2][0])
        self.assertEqual(1, graph.m_adjacency[1][2])
        self.assertEqual(1, graph.m_adjacency[2][1])
