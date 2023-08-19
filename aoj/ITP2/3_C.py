# 3_C.py Count

from sys import stdin
from math import inf

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for line in stdin.readlines():
    b, e, k = [int(e) for e in line.split()]
    print(a[b:e].count(k))
