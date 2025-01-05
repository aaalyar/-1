import time
import random

class Graph:
    def __init__(self):
        self.edges = []  # Инициализация пустого объекта графа
        self.vertices = set()  # Множество для хранения вершин

    def add_vertex(self, vertex):
        self.vertices.add(vertex)

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            self.vertices.remove(vertex)
            self.edges = [edge for edge in self.edges if vertex not in edge]

    def add_edge(self, edge):
        if edge[0] in self.vertices and edge[1] in self.vertices:
            self.edges.append(edge)

    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)

    def find_edge(self, edge):
        return edge in self.edges

    def is_isolated(self, vertex):
        return vertex in self.vertices and all(vertex not in edge for edge in self.edges)


# Функция для тестирования времени выполнения операций
def test_graph_performance():
    sizes = [50, 100]
    for size in sizes:
        print(f"\nТестирование графа с {size} вершинами:")

        # Тест 1: Линейный граф
        print("\n1 граф:")
        graph = Graph()
        start_time = time.time()
        for i in range(size):
            graph.add_vertex(i)
        for i in range(size - 1):
            graph.add_edge((i, i + 1))
        print(f"Время построения 1 графа: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size - 1):
            graph.find_edge((i, i + 1))
        print(f"Время проверки рёбер: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            graph.is_isolated(i)
        print(f"Время проверки изолированности: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size - 1):
            graph.remove_edge((i, i + 1))
        print(f"Время удаления рёбер: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            graph.remove_vertex(i)
        print(f"Время удаления вершин: {time.time() - start_time:.6f} секунд")

        # Тест 2: Плотный граф
        print("\n2 граф:")
        dense_graph = Graph()
        start_time = time.time()
        for i in range(size):
            dense_graph.add_vertex(i)
        for i in range(size):
            for j in range(i + 1, size):
                dense_graph.add_edge((i, j))
        print(f"Время построения 2 графа: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            for j in range(i + 1, size):
                dense_graph.find_edge((i, j))
        print(f"Время проверки рёбер: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            dense_graph.is_isolated(i)
        print(f"Время проверки изолированности: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            for j in range(i + 1, size):
                dense_graph.remove_edge((i, j))
        print(f"Время удаления рёбер: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            dense_graph.remove_vertex(i)
        print(f"Время удаления вершин: {time.time() - start_time:.6f} секунд")

        # Тест 3: Случайный граф
        print("\n3 граф:")
        random_graph = Graph()
        start_time = time.time()
        for i in range(size):
            random_graph.add_vertex(i)
        edge_count = size * (size // 10)
        for _ in range(edge_count):
            v1, v2 = random.sample(range(size), 2)
            random_graph.add_edge((v1, v2))
        print(f"Время построения 3 графа: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for _ in range(edge_count):
            v1, v2 = random.sample(range(size), 2)
            random_graph.find_edge((v1, v2))
        print(f"Время проверки рёбер: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            random_graph.is_isolated(i)
        print(f"Время проверки изолированности: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for _ in range(edge_count):
            v1, v2 = random.sample(range(size), 2)
            random_graph.remove_edge((v1, v2))
        print(f"Время удаления рёбер: {time.time() - start_time:.6f} секунд")

        start_time = time.time()
        for i in range(size):
            random_graph.remove_vertex(i)
        print(f"Время удаления вершин: {time.time() - start_time:.6f} секунд")


# Запуск тестов
test_graph_performance()
