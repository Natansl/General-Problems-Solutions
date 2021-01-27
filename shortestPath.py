import math

class ShortestPath(object):
    def __init__(self, dist, prev):
        self.dist = dist
        self.prev = prev 

def dijkstra(G, s):
    length = len(G)
    dist = prev = Q = []
    for i in range(length):
        dist.append(math.inf)
        prev.append(-1)
        Q.append(i)
    dist[s-1] = 0

    while len(Q) > 0:
        aux = indexes = []
        for i in Q:
            aux.append(dist[i])
            indexes.append(i)
        index = aux.index(min(aux))
        u = indexes[index]
        Q.remove(u)

        for v in range(length):
            if v == u:
                continue
            alt = dist[u] + G[u][v]
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return ShortestPath(dist,prev)

def bellmanFord(G, s):
    length = len(G)
    dist = prev = []
    for _ in range(length):
        dist.append(math.inf)
        prev.append(-1)
    dist[s-1] = 0

    for _ in range(length - 1):
        for u in range(length - 1):
            for v in range(u + 1, length):
                if dist[u] + G[u][v] < dist[v]:
                    dist[v] = dist[u] + G[u][v]
    
    for u in range(length - 1):
            for v in range(u + 1, length):
                if dist[u] + G[u][v] < dist[v]:
                    print("ERROR. Graph with negative weight cycle.")

    return ShortestPath(dist,prev)

def floydWarshall(G):
    length = len(G)
    dist = [[math.inf for i in range(length)] for j in range (length)]

    for i in range(length):
        for j in range(length):
            dist[i][j] = G[i][j]
    
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
        
        


