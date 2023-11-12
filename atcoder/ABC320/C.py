def resolve():
    import sys
    sys.setrecursionlimit(2000000)
    import math
    import collections as cl
    import functools as ft
    import itertools as it
    import operator as op
    from bisect import bisect_left, bisect_right
    from heapq import heappush, heappop

    def fastest(digit):
        done = [False] * 3
        for i, R in enumerate(it.chain(S, S, S)):
            for j in range(3):
                if R[j] == digit:
                    done[j] = True
                    break            
            if all(done): return i
        return float("inf")

    M = int(input())
    S = list(zip(input(), input(), input()))
    
    ans = float("inf")
    for d in "0123456789":
        ans = min(ans, fastest(d))
    print(-1 if ans == float("inf") else ans)

# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """10
1937458062
8124690357
2385760149"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
01234567890123456789
01234567890123456789
01234567890123456789"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
11111
22222
33333"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
