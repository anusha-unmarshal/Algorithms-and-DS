class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [None] * vertices

    def addEdge(self, source, dest):
        # node = Node(source)
        # node.next = self.edges[dest]
        # self.edges[dest] = node

        node = Node(dest)
        node.next = self.edges[source]
        self.edges[source] = node

    def printGraph(self):
        for i in range(self.vertices):
            print("Adjacency list of node "+str(i)+"\nhead", end=" ")
            temp = self.edges[i]
            while temp:
                print("-> {}".format(temp.data), end=" ")
                temp = temp.next
            print()

    def bfs(self,start):
        visited = [False]* (self.vertices)
        queue = []
        queue.append(start)
        visited[start] = True
        while queue:
            start = queue.pop(0)
            print(start, end = " ")
            temp = self.edges[start]
            while temp :
                if visited[temp.data] == False:
                    queue.append(temp.data)
                    visited[temp.data] = True
                temp = temp.next
    
    def dfsUtil(self, start, visited):
        visited.add(start)
        print(start, end=" ")
        temp = self.edges[start]
        while temp:
            if temp.data not in visited:
                self.dfsUtil(temp.data, visited)
            temp = temp.next
            
    def dfs(self,start):
        visited = set()
        
        self.dfsUtil(start, visited)
                

nodes = int(input("Enter number of nodes in graph"))
sampleGraph = graph(nodes)

print("1: Add new edge")
print("2: Print graph")
print("3: Delete Edge")
print("4: BFS Traversal")
print("5: Exit")
while True:
    choice = int(input())
    if choice == 1:
        edge = list(input("Enter source and destination").split())
        # print(edge)
        sampleGraph.addEdge(int(edge[0]),int(edge[1]))
    elif choice == 2:
        sampleGraph.printGraph()
    # elif choice == 3:
    #     edge = list(input("Enter source and distination").split())
    #     # print(edge)
    #     sampleGraph.deleteEdge(int(edge[0]),int(edge[1]))
    elif choice == 4:
        start = int(input("Enter starting point"))
        sampleGraph.bfs(start)
    elif choice == 5:
        start = int(input("Enter the starting point"))
        sampleGraph.dfs(start)
    else:
        break
