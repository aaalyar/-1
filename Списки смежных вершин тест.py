import time

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            del self.adjacency_list[vertex]
            for v in self.adjacency_list:
                if vertex in self.adjacency_list[v]:
                    self.adjacency_list[v].remove(vertex)

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                self.adjacency_list[vertex1].remove(vertex2)
            if vertex1 in self.adjacency_list[vertex2]:
                self.adjacency_list[vertex2].remove(vertex1)

    def find_edge(self, vertex1, vertex2):
        return vertex2 in self.adjacency_list.get(vertex1, [])

    def is_isolated(self, vertex):
        return vertex in self.adjacency_list and len(self.adjacency_list[vertex]) == 0

# Тестирование производительности
def performance_test():
    graph = Graph()
    
    # Замер времени добавления вершин
    start_time = time.time()
    for i in range(1000):
        graph.add_vertex(i)
    print(f"Время добавления 1000 вершин: {time.time() - start_time:.6f} секунд")

    # Замер времени добавления рёбер
    start_time = time.time()
    for i in range(1000):
        graph.add_edge(i, (i + 1) % 1000)
    print(f"Время добавления 1000 рёбер: {time.time() - start_time:.6f} секунд")

    # Замер времени удаления вершин
    start_time = time.time()
    for i in range(500):
        graph.remove_vertex(i)
    print(f"Время удаления 500 вершин: {time.time() - start_time:.6f} секунд")

    # Замер времени удаления рёбер
    start_time = time.time()
    for i in range(500):
        graph.remove_edge(i, (i + 1) % 1000)
    print(f"Время удаления 500 рёбер: {time.time() - start_time:.6f} секунд")

# Запуск тестирования
performance_test()
