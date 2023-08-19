# 4_D.py Unique

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]

print(*sorted(set(a)))
