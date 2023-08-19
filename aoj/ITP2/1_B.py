# 1_B.py Deque

from sys import stdin
from collections import deque

def push(dq, d, x):
    (dq.appendleft if d == 0 else dq.append)(x)

def random_access(dq, p):
    print(dq[p])

def pop(dq, d):
    (dq.popleft if d == 0 else dq.pop)()

_ = int(input())
dq = deque()

perform_query = [push, random_access, pop]
for query in stdin.readlines():
    order, *args = [int(e) for e in query.split()]
    perform_query[order](dq, *args)
