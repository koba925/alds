# 4_D.py

from sys import stdin
from math import floor

def bisect(ng, ok, is_ok):
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

def solve():

    n, k = [int(e) for e in stdin.readline().split()]
    w = [int(e) for e in stdin.readlines()]

    def is_ok(P):
        load = 0
        l = 0
        for wi in w:
            if wi > P:
                return False
            if load + wi > P:
                l += 1
                if l == k:
                    return False
                load = 0
            load += wi
        return True

    ng = max(floor(sum(w) / k), max(w)) - 1
    ok = sum(w)
    print(bisect(ng, ok, is_ok))

solve()