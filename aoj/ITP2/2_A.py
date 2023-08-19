# 2_A.py Stack
# list: .55s
# deque: 0.58s

from sys import stdin
from collections import deque

n, q = [int(e) for e in stdin.readline().split()]

stacks = [deque() for _ in range(n)]

for query in stdin.readlines():
    command, t, *param = [int(e) for e in query.split()]
    if command == 0:
        stacks[t].append(param[0])
    elif command == 1 and len(stacks[t]) > 0:
        print(stacks[t][-1])
    elif len(stacks[t]) > 0:
        stacks[t].pop()
