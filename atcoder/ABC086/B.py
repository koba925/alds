# B - 1 21

from sys import stdin

def is_squared_short(a, b):
    ab = int(str(a) + str(b))
    return (ab ** 0.5 // 1) ** 2 == ab

def unite(a, b):
    c = b
    while c > 0:
        a *= 10
        c //= 10
    return a + b

def is_squared(a, b):
    ab = unite(a, b)
    return any([n * n == ab for n in range(1, int(100100 ** 0.5))])

def solve2():
    a, b = [int(e) for e in stdin.readline().split()]
    print("Yes" if is_squared(a, b) else "No")

def solve():
    a, b = stdin.readline().split()
    ab = int(a + b)
    print("Yes" if (ab ** 0.5 // 1) ** 2 == ab else "No")

solve()
