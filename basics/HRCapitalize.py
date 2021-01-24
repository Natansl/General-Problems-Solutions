import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    seg = s.split(" ")
    out = ""
    for sub in seg:
        if not sub:
            out += " "
        else:
            initial = str(sub[0])
            initial = initial.upper()
            out +=  initial + sub[1:] + " "
    return out

s = "hello   world  lol"
print(solve(s))