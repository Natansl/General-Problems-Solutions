#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    r_q -= 1
    c_q -= 1
    total = 0
    for i in range (n):
        for j in range(n):
            if i == r_q or j == c_q or abs(r_q - i) == abs(c_q - j):
                total += 1  
    total -= 1
    
    for obs in obstacles:
        obs[0] -= 1
        obs[1] -= 1
        if abs(obs[0] - r_q) == abs(obs[1] - c_q):
            if obs[0] > r_q and obs[1] > c_q:
                total -= min(n - 1 - c_q, n - 1 - r_q)
            elif obs[0] > r_q and obs[1] < c_q:
                total -= min(n - 1 - r_q, c_q)
            elif obs[0] < r_q and obs[1] > c_q:
                total -= min(n - 1 - c_q, r_q)
            else:
                total -= min(c_q, r_q)
            total += 1
        elif obs[0] == r_q:
            if obs[1] > c_q:
                total -= n - obs[1]
            else:
                total -= obs[1] + 1
        elif obs[1] == c_q:
            if obs[0] > r_q:
                total -= n - obs[0]
            else:
                total -= obs[0] + 1
    return total
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])

    c_q = int(r_qC_q[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
