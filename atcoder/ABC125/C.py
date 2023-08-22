# LL: GCD(0, a) = a

import sys  # https://docs.python.org/ja/3/library/sys.html
import math  # https://docs.python.org/ja/3/library/math.html


def blackboard(N, A):
    A = [0] + A + [0]
    left_gcd, right_gcd = [0] * (N + 2), [0] * (N + 2)
    for i in range(1, N + 1):
        left_gcd[i] = math.gcd(left_gcd[i - 1], A[i])
    for i in reversed(range(1, N + 1)):
        right_gcd[i] = math.gcd(right_gcd[i + 1], A[i])

    max_gcd = 0
    for i in range(1, N + 1):
        max_gcd = max(max_gcd, math.gcd(left_gcd[i - 1], right_gcd[i + 1]))

    return max_gcd


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print(blackboard(N, A))


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

    def test_1(self):
        input = """2
6 8"""
        output = """8"""
        self.assertIO(input, output)

    def test_2(self):
        input = """3
1 1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_3(self):
        input = """8
746130 1385670 4849845 881790 3233230 1939938 570570 510510"""
        output = """19"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3
7 6 8"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
12 15 18"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()


# 746130, 1385670, 4849845, 881790, 3233230, 1939938, 570570, 510510

# import sys  # https://docs.python.org/ja/3/library/sys.html
# import functools as ft  # https://docs.python.org/ja/3/library/functools.html
# import math  # https://docs.python.org/ja/3/library/math.html


# def gcd_on_blackboard(N, A):
#     A = [0] + A + [0]
#     left_gcd = [0] * (N + 2)
#     for i in range(1, N + 1):
#         left_gcd[i] = math.gcd(left_gcd[i - 1], A[i])

#     right_gcd = [0] * (N + 2)
#     for i in reversed(range(1, N + 1)):
#         right_gcd[i] = math.gcd(A[i], right_gcd[i + 1])

#     return max(math.gcd(l, r) for l, r in zip(left_gcd[:-2], right_gcd[2:]))


# def resolve():
#     N = int(sys.stdin.readline())
#     A = [int(e) for e in sys.stdin.readline().split()]
#     print(gcd_on_blackboard(N, A))


# # resolve()
# # exit()
