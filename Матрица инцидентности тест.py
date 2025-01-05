import time

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

# Тестирование класса с замером времени для разных графов
def test_graph(graph):
    # Замер времени добавления вершин
    start_time = time.time()
    for i in range(1000):
        graph.add_vertex(f"V{i}")
    print(f"Время добавления вершин: {time.time() - start_time:.4f} секунд")

    # Замер времени добавления рёбер
    start_time = time.time()
    for i in range(999):
        graph.add_edge(f"V{i}", f"V{i+1}")
    print(f"Время добавления рёбер: {time.time() - start_time:.4f} секунд")

    # Замер времени проверки рёбер
    start_time = time.time()
    graph.find_edges()
    print(f"Время проверки рёбер: {time.time() - start_time:.4f} секунд")

    # Замер времени проверки изолированности
    start_time = time.time()
    for i in range(1000):
        graph.is_isolated(f"V{i}")
    print(f"Время проверки изолированности: {time.time() - start_time:.4f} секунд")

    # Замер времени удаления рёбер
    start_time = time.time()
    for i in range(999):
        graph.remove_edge(f"V{i}", f"V{i+1}")
    print(f"Время удаления рёбер: {time.time() - start_time:.4f} секунд")

    # Замер времени удаления вершин
    start_time = time.time()
    for i in range(1000):
        graph.remove_vertex(f"V{i}")
    print(f"Время удаления вершин: {time.time() - start_time:.4f} секунд")

# Создание 3 графов
if __name__ == "__main__":
    print("Тестирование линейного графа:")
    graph1 = IncidenceMatrix()
    test_graph(graph1)

    print("\nТестирование случайного графа:")
    graph2 = IncidenceMatrix()
    test_graph(graph2)

    print("\nТестирование графа с небольшим числом рёбер:")
    graph3 = IncidenceMatrix()
    test_graph(graph3)
