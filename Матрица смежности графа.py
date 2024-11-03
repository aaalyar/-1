class Graph:
    def __init__(self):
        self.adjacency_matrix = []
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = len(self.adjacency_matrix)
            for row in self.adjacency_matrix:
                row.append(0)
            self.adjacency_matrix.append([0] * (len(self.adjacency_matrix) + 1))

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            index = self.vertices[vertex]
            self.adjacency_matrix.pop(index)
            for row in self.adjacency_matrix:
                row.pop(index)
            del self.vertices[vertex]
            self.vertices = {v: (i if i < index else i - 1) for v, i in self.vertices.items()}

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_matrix[self.vertices[vertex1]][self.vertices[vertex2]] = 1
            self.adjacency_matrix[self.vertices[vertex2]][self.vertices[vertex1]] = 1  # Для неориентированного графа

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.adjacency_matrix[self.vertices[vertex1]][self.vertices[vertex2]] = 0
            self.adjacency_matrix[self.vertices[vertex2]][self.vertices[vertex1]] = 0  # Для неориентированного графа

    def has_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            return self.adjacency_matrix[self.vertices[vertex1]][self.vertices[vertex2]] == 1
        return False

    def is_isolated(self, vertex):
        if vertex in self.vertices:
            index = self.vertices[vertex]
            return all(edge == 0 for edge in self.adjacency_matrix[index])
        return False
