# 4_C.py Swap

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for line in stdin.readlines():
    b, e, t = [int(e) for e in line.split()]
    a[b:e], a[t:t+(e-b)] = a[t:t+(e-b)], a[b:e]

print(*a)
