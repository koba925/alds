import sys  # https://docs.python.org/ja/3/library/sys.html
import functools as ft  # https://docs.python.org/ja/3/library/functools.html
import math  # https://docs.python.org/ja/3/library/math.html


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print(math.gcd(A))


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
        input = """4
2 10 8 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 13 8 1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1000000000 1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

# import sys
# from math import gcd

# def monsters(N, A):
#     g = A[0]
#     for a in A[1:]:
#         g = gcd(g, a)
#     return g

# def resolve():
#     N = int(sys.stdin.readline())
#     A = [int(e) for e in sys.stdin.readline().split()]
#     print(monsters(N, A))

# resolve()
# exit()
