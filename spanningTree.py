import math
from operator import itemgetter

def Prim(G, v):
    V = len(G)
    connected = [0 for i in range(V)]
    Gout = [[math.inf for i in range(V)] for j in range(V)]
    considered = []
    indexes = []
    connected[v-1] = 1
    i = v-1
    while connected.count(0) > 0:
        for j in range(V):
            if j == i:
                continue
            if not connected[j]:
                considered.append(G[i][j])
                indexes.append([i, j])

        minimum = math.inf
        minIndex = math.inf
        for k in range (len(considered)):
            if considered[k] < minimum and (not connected[indexes[k][0]] or not connected[indexes[k][1]]):
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
        curri = idx[indexes.find(i)][0]
        currj = idx[indexes.find(i)[1]
        if not connected[curri] or not connected[currj]:
            connected[curri] = 1
            connected[currj] = 1
            Gout[curri][currj] = considered[indexes.find(i)
            Gout[currj][curri] = considered[indexes.find(i)
        i += 1

    return Gout

G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]
v = 5
print("Prim Algorithm: " + str(Prim(G,v)))
print("Kruskal Algorithm: " + str(Kruskal(G)))
