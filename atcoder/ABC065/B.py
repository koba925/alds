# B.py

def find(a):
    visited = [None] + [False] * len(a)
    i = 1
    k = 0
    while not visited[i]:
        if a[i] == 2:
            return k + 1
        visited[i] = True
        i = a[i]
        k += 1
    return -1

from sys import stdin

n = int(stdin.readline())
a = [0] + [int(e) for e in stdin.readlines()]
print(find(a))
