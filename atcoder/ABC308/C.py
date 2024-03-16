# TK:比較関数を渡してソート

import sys
from io import StringIO
import unittest


def resolve():
    import functools as ft

    def cmp(l, r):
        _, [a1, b1] = l
        _, [a2, b2] = r
        L = a1 * (a2 + b2)
        R = a2 * (a1 + b1)
        return 1 if L < R else -1 if L > R else 0

    N = int(input())
    AB = [[int(e) for e in input().split()] for _ in range(N)]
    S = sorted(enumerate(AB, 1), key=ft.cmp_to_key(cmp))
    print(*[i for i, _ in S])


class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """2
1 0
1 0"""
        output = """1 2"""
        self.assertIO(input, output)
    
    def test_my_2(self):
        input = """2
1 0
0 1"""
        output = """1 2"""
        self.assertIO(input, output)
    
    def test_sample1(self):
        input = """3
1 3
3 1
2 2"""
        expected = """2 3 1"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """2
1 3
2 6"""
        expected = """1 2"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """4
999999999 1000000000
333333333 999999999
1000000000 999999997
999999998 1000000000"""
        expected = """3 1 4 2"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
