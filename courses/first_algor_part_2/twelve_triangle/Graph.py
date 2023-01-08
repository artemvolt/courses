class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class SimpleGraph:

    def __init__(self, size: int):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v) -> bool:
        # ваш код добавления новой вершины
        # с значением value
        # в свободное место массива vertex
        if None not in self.vertex:
            return False

        index = self.vertex.index(None)
        self.vertex[index] = Vertex(v)
        return True

    # здесь и далее, параметры v -- индекс вершины
    # в списке  vertex
    def RemoveVertex(self, v: int):
        # ваш код удаления вершины со всеми её рёбрами
        self.vertex[v] = None
        for i in range(self.max_vertex):
            self.m_adjacency[i][v] = 0
            self.m_adjacency[v][i] = 0

    def IsEdge(self, v1: int, v2: int) -> bool:
        # True если есть ребро между вершинами v1 и v2
        return self.m_adjacency[v1][v2] == 1

    def AddEdge(self, v1: int, v2: int) -> None:
        # добавление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1: int, v2: int) -> None:
        # удаление ребра между вершинами v1 и v2
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def DepthFirstSearch(self, VFrom: int, VTo: int) -> list:
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету

        for vertexItem in self.vertex:
            if vertexItem is not None:
                vertexItem.Hit = False

        current = VFrom
        stack = []
        while current is not None:
            current_vertex = self.vertex[current]
            if current_vertex.Hit is False:
                current_vertex.Hit = True
                stack.append(current)

            if self.IsEdge(current, VTo):
                stack.append(VTo)
                current = None
                continue

            is_have_none_hit = False
            for index, item in enumerate(self.vertex):
                if self.IsEdge(current, index) and item.Hit is False:
                    current = index
                    is_have_none_hit = True
                    break

            if is_have_none_hit is True:
                continue

            stack.pop(0)

            if len(stack) == 0:
                return []

            current = stack[-1]
            self.vertex[current].Hit = True

        result = []
        for idx in stack:
            result.append(self.vertex[idx])

        return result

    def BreadthFirstSearch(self, VFrom, VTo):
        # узлы задаются позициями в списке vertex
        # возвращается список узлов -- путь из VFrom в VTo
        # или [] если пути нету
        for vertexItem in self.vertex:
            if vertexItem is not None:
                vertexItem.Hit = False

        current = VFrom
        queue = []
        path = {}
        self.vertex[current].Hit = True
        path[current] = [current]

        while current is not None:
            if self.IsEdge(current, VTo):
                p = path[current].copy()
                p.append(VTo)
                path[VTo] = p
                path.pop(current)
                current = None
                continue

            is_have_none_hit = False
            for index, item in enumerate(self.vertex):
                if self.IsEdge(current, index) and item.Hit is False:
                    is_have_none_hit = True
                    item.Hit = True
                    queue.append(index)
                    p = path[current].copy()
                    p.append(index)
                    path[index] = p

            if is_have_none_hit is True:
                path.pop(current)
            if len(queue) == 0:
                return []
            else:
                current = queue.pop(0)

        result = []
        for idx in path[VTo]:
            result.append(self.vertex[idx])

        return result

    def WeakVertices(self) -> list:
        # возвращает список узлов вне треугольников
        outside_the_triangle = []
        for index_vertex, vertex in enumerate(self.vertex):
            edges_indexes = []
            for index_vertex_compare, vertex_compare in enumerate(self.vertex):
                if self.IsEdge(index_vertex, index_vertex_compare):
                    edges_indexes.append(index_vertex_compare)

            if len(edges_indexes) < 2:
                outside_the_triangle.append(self.vertex[index_vertex])
                continue

            count = 0
            for edge_index in edges_indexes:
                for edge_index_compare in edges_indexes:
                    if count == 2:
                        break

                    if self.IsEdge(edge_index, edge_index_compare):
                        count += 1

            if count != 2:
                outside_the_triangle.append(self.vertex[index_vertex])

        return outside_the_triangle
