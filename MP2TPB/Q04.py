# Q04.py 棒の切り分け

from math import ceil

def solve1(n, m):
    count = 0
    current = 1
    while current < m and current <= n // 2:
        count += 1
        current *= 2
    return count + ceil((n - current) / m) 

def solve2(n, m):
    def _solve2(current):
        if current >= n:
            return 0
        if current <= m:
            return 1 + _solve2(current * 2)
        return 1 + _solve2(current + m)
    return _solve2(1)

def solve3(n, m):
    count = 0
    current = 1
    while current < n:
        current += current if current < m else m
        count += 1
    return count

print(solve3(8, 3))
print(solve3(20, 3))
print(solve3(100, 5))

from sys import setrecursionlimit
from random import randrange

setrecursionlimit(10000)

for _ in range(10000):
    n = randrange(1, 1000)
    m = randrange(1, 100)
    a1 = solve1(n, m)
    a2 = solve2(n, m)
    a3 = solve3(n, m)
    if not a1 == a2 == a3:
        print("wrong:", n, m, a1, a2, a3)
