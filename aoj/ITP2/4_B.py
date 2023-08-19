# 4_B.py Rotate

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for line in stdin.readlines():
    b, m, e = [int(e) for e in line.split()]
    a[b:e] = a[m:e] + a[b:m]

print(*a)