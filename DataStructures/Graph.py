import math

class Graph(object):
    def __init__(self, adjMatrix):
        self.adjMatrix = adjMatrix
        length = len(adjMatrix)
        adjList = [[] for _ in range(length)]
        for i in range(length - 1):
            for j in range(i + 1, length):
                val = adjMatrix[i][j]
                if val < math.inf:
                    adjList[i].append([j, val])
                    adjList[j].append([i, val])
    
    
    