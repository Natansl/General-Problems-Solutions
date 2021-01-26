import math
from operator import itemgetter

def Prim(G, v):
    V = len(G)
    connected = [0 for i in range(V)]
    Gout = [[math.inf for i in range(V)] for j in range(V)]
    considered = []
    indexes = []
    connected[v-1] = 1
    i = v
    while connected.count(0) > 0:
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

        if connected[indexes[minIndex][0]]:
            i = indexes[minIndex][1]
        else:
            i = indexes[minIndex][0]

        connected[indexes[minIndex][0]] = 1
        connected[indexes[minIndex][1]] = 1
        Gout[indexes[minIndex][0]][indexes[minIndex][1]] = minimum
        Gout[indexes[minIndex][1]][indexes[minIndex][0]] = minimum
        del considered[minIndex]
        del indexes[minIndex]
    return Gout

def Kruskal(G):
    V = len(G)
    connected = [0 for i in range(V)]
    Gout = [[math.inf for i in range(V)] for j in range(V)]
    considered = []
    idx = []

    for i in range(V):
        for j in range(i+1,V):
            considered.append(G[i][j])
            idx.append([i, j])

    indexes, _ = zip(*sorted(enumerate(considered), key=itemgetter(1)))
    i = 0
    while connected.count(0) > 0:
        curri = idx[indexes[i]][0]
        currj = idx[indexes[i]][1]
        if not connected[curri] or not connected[currj]:
            connected[curri] = 1
            connected[currj] = 1
            Gout[curri][currj] = considered[indexes[i]]
            Gout[currj][curri] = considered[indexes[i]]
        i += 1

    return Gout
