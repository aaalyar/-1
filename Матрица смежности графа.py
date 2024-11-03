class IncidenceMatrix:
    def __init__(self):
        self.vertices = []  # Список вершин
        self.edges = []     # Список рёбер
        self.incidence_matrix = []  # Матрица инцидентности

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
            # Обновляем матрицу инцидентности
            for row in self.incidence_matrix:
                row.append(0)
            self.incidence_matrix.append([0] * len(self.vertices))

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            index = self.vertices.index(vertex)
            self.vertices.remove(vertex)
            self.incidence_matrix.pop(index)
            for row in self.incidence_matrix:
                row.pop(index)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.edges.append((vertex1, vertex2))
            index1 = self.vertices.index(vertex1)
            index2 = self.vertices.index(vertex2)
            self.incidence_matrix[index1][-1] = 1
            self.incidence_matrix[index2][-1] = 1
            for row in self.incidence_matrix:
                row.append(0)
            self.incidence_matrix[index1][-1] = 1
            self.incidence_matrix[index2][-1] = 1

    def remove_edge(self, vertex1, vertex2):
        if (vertex1, vertex2) in self.edges:
            self.edges.remove((vertex1, vertex2))
            index1 = self.vertices.index(vertex1)
            index2 = self.vertices.index(vertex2)
            self.incidence_matrix[index1][-1] = 0
            self.incidence_matrix[index2][-1] = 0

    def find_edges(self):
        return self.edges

    def is_isolated(self, vertex):
        if vertex in self.vertices:
            index = self.vertices.index(vertex)
            return all(value == 0 for value in self.incidence_matrix[index])
        return False
