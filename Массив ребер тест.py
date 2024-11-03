import time

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

# Тестирование класса Graph с замером времени
def test_graph_performance():
    graph = Graph()
    
    # Замер времени добавления вершин
    start_time = time.time()
    for i in range(1000):
        graph.add_vertex(i)
    print(f"Время добавления 1000 вершин: {time.time() - start_time:.6f} секунд")

    # Замер времени добавления рёбер
    start_time = time.time()
    for i in range(999):
        graph.add_edge((i, i + 1))
    print(f"Время добавления 999 рёбер: {time.time() - start_time:.6f} секунд")

    # Замер времени удаления вершин
    start_time = time.time()
    for i in range(500):
        graph.remove_vertex(i)
    print(f"Время удаления 500 вершин: {time.time() - start_time:.6f} секунд")

    # Замер времени удаления рёбер
    start_time = time.time()
    for i in range(500):
        graph.remove_edge((i, i + 1))
    print(f"Время удаления 500 рёбер: {time.time() - start_time:.6f} секунд")

# Запуск тестирования
test_graph_performance()
