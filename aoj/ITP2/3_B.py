# 3_B.py Min-Max

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for line in stdin.readlines():
    query = [int(e) for e in line.split()]
    if query[0] == 0:
        print(min(a[query[1]:query[2]]))
    elif query[0] == 1:
        print(max(a[query[1]:query[2]]))

