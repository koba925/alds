# 4_A.py Reverse

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for line in stdin.readlines():
    b, e = [int(e) for e in line.split()]
    a[b:e] = reversed(a[b:e])

print(*a)