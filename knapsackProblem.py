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

def kspGreedy(items,capacity):
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

items = [[60, 10], [100, 20], [120, 30]]
capacity = 50
print("Bruteforce Exact Solution: " + str(kspbruteForce(items, capacity)))
print("Greedy Approximation algorithm: " + str(kspGreedy(items, capacity)))