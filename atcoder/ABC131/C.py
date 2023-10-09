import math

def nums_in_range(n, a, b):
    return b // n - (a - 1) // n

def resolve_mine():
    A, B, C, D = [int(e) for e in input().split()]
    N = B - A + 1
    L = math.lcm(C, D)
    print(N - nums_in_range(C, A, B) - nums_in_range(D, A, B) + nums_in_range(L, A, B))

def nums_ok(a, c, d):
    l = math.lcm(c, d)
    return a - a // c - a // d + a // l

def resolve():
    A, B, C, D = [int(e) for e in input().split()]
    print(nums_ok(B, C, D) - nums_ok(A - 1, C, D))

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
        input = """4 9 2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 40 6 8"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """314159265358979323 846264338327950288 419716939 937510582"""
        output = """532105071133627368"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
