class Graph:
    def __init__(self):
        self.adj_list = {} 
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
    
    def add_edge(self, src, dest):
        self.add_vertex(src)
        self.add_vertex(dest)
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)  
    
    def display(self):
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        print("BFS:", end=" ")
        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

graph = Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(2, 5)

print("Graph adjacency list:")
graph.display()
print()

graph.bfs(1)
print()
