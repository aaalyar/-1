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
