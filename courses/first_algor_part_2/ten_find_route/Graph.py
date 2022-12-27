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
            vertexItem.Hit = False

        stack = []
        fromItem = self.vertex[VFrom]
        fromItem.Hit = True
        stack.append(fromItem)

        if self.IsEdge(VFrom, VTo):
            stack.append(self.vertex[VTo])
            return stack

        foundVTo = self.FindNearestNoneHitVertex(VTo)
        if foundVTo != VTo:
            stack = stack + self.DepthFirstSearch(foundVTo, VTo)

        if foundVTo is None:
            stack.pop()

        if len(stack) == 0:
            return []

        return stack

    def FindNearestNoneHitVertex(self, vertexIndex: int):
        for anotherIndex, anotherVertex in enumerate(self.vertex):
            if anotherIndex != vertexIndex and anotherVertex.Hit is False:
                return anotherIndex
        return None
