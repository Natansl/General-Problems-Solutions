import math

class ShortestPath(object):
    def __init__(self, dist, prev):
        self.dist = dist
        self.prev = prev 

def Dijkstra(G, s):
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
        
        


