# 1_D.py Vector II

from sys import stdin

n, q = [int(e) for e in stdin.readline().split()]
A = [[] for _ in range(n)]

for line in stdin.readlines():
    query = [int(e) for e in line.split()]
    if query[0] == 0:
        A[query[1]].append(query[2])
    elif query[0] == 1:
        print(*A[query[1]])
    else:
        A[query[1]].clear()
