from operator import itemgetter
import math

def Prim(G, v):
    V = len(G)
    connected = [0 for i in range(V)]
    Gout = [[math.inf for i in range(V)] for j in range(V)]
    considered = []
    indexes = []
    connected[v-1] = 1
    while (connected.count(0) > 0):
        for i in range(V):
            if not connected[i]:
                continue
            for j in range(V):
                if j == i:
                    continue
                if not connected[j]:
                    considered.append(G[i][j])
                    indexes.append([i, j])

        minimum = considered[0]
        minIndex = 0
        for k in range (1,len(considered)):
            if considered[k] < minimum and (not connected[i] or not connected[j]):
                minimum = considered[k]
                minIndex = k
        connected[indexes[minIndex][0]] = 1
        connected[indexes[minIndex][1]] = 1
        Gout[indexes[minIndex][0]][indexes[minIndex][1]] = minimum
        Gout[indexes[minIndex][1]][indexes[minIndex][0]] = minimum
        del considered[minIndex]
        del indexes[minIndex]
    return Gout
