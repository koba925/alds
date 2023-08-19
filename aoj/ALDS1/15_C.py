# 15_C.py Activity Selection Problem

from sys import stdin

n = int(stdin.readline())
acts = [[int(e) for e in line.split()] for line in stdin.readlines()]

acts.sort(key=lambda e: e[1])
ans, last = 0, -1
for s, t in acts:
    if last < s:
        ans += 1
        last = t
print(ans)
