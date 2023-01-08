import unittest
import sys

sys.path.append('/var/www/courses')

from courses.first_algor_part_2.twelve_triangle.Graph import SimpleGraph, Vertex


class GraphTest(unittest.TestCase):
    def create_graph(self, items: list) -> SimpleGraph:
        graph = SimpleGraph(len(items))
        for item in items:
            graph.AddVertex(item)
        return graph

    def vertex_list_to_list_values(self, items: list) -> list:
        return list(
            map(
                lambda x: x.Value,
                items
            )
        )

    def test_weak_vertices(self):
        graph = self.create_graph([1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        self.assertEqual([1, 2, 3], self.vertex_list_to_list_values(graph.WeakVertices()))

        graph = self.create_graph([1, 2, 3])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)
        self.assertEqual([], self.vertex_list_to_list_values(graph.WeakVertices()))

        graph = self.create_graph([1, 2, 3, 4, 5, 6])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        graph.AddEdge(3, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(2, 3)
        self.assertEqual([4, 5, 6], self.vertex_list_to_list_values(graph.WeakVertices()))

        graph = self.create_graph([1, 2, 3, 4, 5, 6])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        graph.AddEdge(3, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(2, 3)
        graph.AddEdge(4, 5)
        self.assertEqual([], self.vertex_list_to_list_values(graph.WeakVertices()))

        graph = self.create_graph([1, 2, 3, 4, 5, 6, 7])
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(1, 2)

        graph.AddEdge(3, 4)
        graph.AddEdge(3, 5)
        graph.AddEdge(2, 3)
        graph.AddEdge(4, 5)
        graph.AddEdge(3, 6)
        self.assertEqual([7], self.vertex_list_to_list_values(graph.WeakVertices()))
