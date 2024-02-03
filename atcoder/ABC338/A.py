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

    S = input()
    print("Yes" if S[0].isupper() and (len(S) == 1 or S[1:].islower()) else "No")

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
        input = """Capitalized"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AtCoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """yes"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """A"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
