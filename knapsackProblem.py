

def __BFRecursive__(items, capacity, w, v, start):
    solutions = []
    for i in range(start, len(items)):
        if w + items[i][1] <= capacity:
            solutions.append(__BFRecursive__(items, capacity, w + items[i][1], v + items[i][0], i + 1))
    solutions.append(v)
    return max(solutions)

def bruteForce(items, capacity):
    solutions = []
    length = len(items)
    for i in range(length):
        w = items[i][1]
        v = items[i][0]
        solutions.append(__BFRecursive__(items, capacity, w, v, i + 1))
    return max(solutions)

items = [[60, 10], [100, 20], [120, 30]]
capacity = 50
print(bruteForce(items, capacity))