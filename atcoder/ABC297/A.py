def resolve():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    import sys
    import math
    import collections as cl
    import functools as ft
    import itertools as it
    import operator as op
    import bisect as bs
    import heapq as hq
    # https://grantjenks.com/docs/sortedcontainers/sortedset.html
    # https://qiita.com/Shirotsume/items/706742162db68c481c3c
    from sortedcontainers import SortedSet, SortedList, SortedDict

    sys.setrecursionlimit(2000000)

    N, D = [int(e) for e in input().split()]
    T = [int(e) for e in input().split()]

    for x1, x2 in it.pairwise(T):
        if x2 - x1 <= D:
            print(x2)
            break
    else:
        print(-1)

def resolve():
    import itertools as it

    N, D = [int(e) for e in input().split()]
    T = [int(e) for e in input().split()]

    print(([x2 for x1, x2 in it.pairwise(T) if x2 - x1 <= D] or [-1])[0])

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
        input = """4 500
300 900 1300 1700"""
        output = """1300"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 99
100 200 300 400 500"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 500
100 600 1100 1600"""
        output = """600"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
