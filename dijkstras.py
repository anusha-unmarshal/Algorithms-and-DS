import sys

class graph():
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [[0 for column in range(vertices)] for column in range(vertices)]

    def printSolution(self,dist):
        for node in range(self.vertices):
            print(node, "->", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        for v in range(self.vertices):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize]*self.vertices
        dist[src] = 0
        sptSet = [False]*self.vertices

        for cout in range(self.vertices):
            u = self.minDistance(dist,sptSet)

            sptSet[u] = True

            for v in range(self.vertices):
                if self.edges[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.edges[u][v]:
                    dist[v] = dist[u] + self.edges[u][v]
        
        self.printSolution(dist)

g = graph(9)
g.edges = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
g.dijkstra(0)