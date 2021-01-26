from operator import itemgetter

def __kspBFRecursive__(items, capacity, w, v, start):
    solutions = []
    for i in range(start, len(items)):
        if w + items[i][1] <= capacity:
            solutions.append(__kspBFRecursive__(items, capacity, w + items[i][1], v + items[i][0], i + 1))
    solutions.append(v)
    return max(solutions)

def kspbruteForce(items, capacity):
    solutions = []
    length = len(items)
    for i in range(length):
        w = items[i][1]
        v = items[i][0]
        solutions.append(__kspBFRecursive__(items, capacity, w, v, i + 1))
    return max(solutions)

def kspGreedy(items, capacity):
    acc = 0
    solution = 0
    costBenefit = [int(items[i][0]/items[i][1]) for i in range(len(items))]
    indexes, _ = zip(*sorted(enumerate(costBenefit), key=itemgetter(1)))
    length = len(indexes)
    for i in range(length):
        acc += items[indexes[length - 1 -i]][1]
        if acc <= capacity:
            solution += items[indexes[length - 1 -i]][0]
        else:
            return solution
    return solution

def kspDynProg(items, capacity):
    m = [[0 for col in range(capacity + 1)] for row in range(len(items) + 1)]
    for j in range(capacity + 1):
        m[0][j] = 0
    for i in range(len(items)):
        for j in range(capacity + 1):
            if items[i][1] > j:
                m[i+1][j] = m[i][j]
            else:
                m[i+1][j] = max([m[i][j], m[i][j - items[i][1]] + items[i][0]])
    return m[len(items)][capacity]

def frackspGreedy(items, capacity):
    acc = 0
    solution = 0
    costBenefit = [int(items[i][0]/items[i][1]) for i in range(len(items))]
    indexes, _ = zip(*sorted(enumerate(costBenefit), key=itemgetter(1)))
    length = len(indexes)
    for i in range(length):
        acc += items[indexes[length - 1 -i]][1]
        if acc <= capacity:
            solution += items[indexes[length - 1 -i]][0]
        else:
            solution += items[indexes[length - 1 -i]][0] * (items[indexes[length - 1 -i]][1] - (acc-capacity))/items[indexes[length - 1 -i]][1]
            return solution
    return solution

items = [[60, 10], [100, 20], [120, 30]]
capacity = 50
print("KSP: ")
print("Bruteforce Solution: " + str(kspbruteForce(items, capacity)))
print("Greedy Approximation algorithm: " + str(kspGreedy(items, capacity)))
print("Dynamic Programming Solution: " + str(kspDynProg(items, capacity)))

print("\nFractional KSP: ")
print("Greedy Solution: " + str(frackspGreedy(items, capacity)))