# import numpy as np
class graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.matrix = [[0 for i in range(nodes)] for j in range(nodes)]
    
    def addEdge(self, fromNode, toNode):
        self.matrix[fromNode][toNode] = 1
        self.matrix[toNode][fromNode] = 1
    
    def deleteEdge(self, fromNode, toNode):
        self.matrix[fromNode][toNode] = 0
        self.matrix[toNode][fromNode] = 0

    def printGraph(self):
        for fromNode in range(self.nodes):
             for toNode in range(self.nodes):
                 print(self.matrix[fromNode][toNode],end = " ")
             print()

nodes = int(input("Enter number of nodes in graph"))
sampleGraph = graph(nodes)

print("1: Add new edge")
print("2: Print graph")
print("3: Delete Edge")
print("4: Exit")
while True:
    choice = int(input())
    if choice == 1:
        edge = list(input("Enter source and destination").split())
        # print(edge)
        sampleGraph.addEdge(int(edge[0]),int(edge[1]))
    elif choice == 2:
        sampleGraph.printGraph()
    elif choice == 3:
        edge = list(input("Enter source and distination").split())
        # print(edge)
        sampleGraph.deleteEdge(int(edge[0]),int(edge[1]))
    else:
        break