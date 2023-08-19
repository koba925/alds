# 15_B.py Fractional Knapsack Problem

from sys import stdin
from typing import List, Tuple

def max_value(W: int, items:List[List[int]]) -> float:
    items = sorted(items, key=lambda e: e[0] / e[1], reverse=True)
    total = 0.0
    for v, w in items:
        if W < w:
            total += v * W / w
            break
        W -= w
        total += v
    return total

N, W = [int(e) for e in stdin.readline().split()]
items = [[int(e) for e in line.split()] for line in stdin.readlines()]

print(max_value(W, items))
