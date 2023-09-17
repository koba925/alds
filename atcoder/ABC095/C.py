import sys


def resolve():
    A, B, C, X, Y = [int(e) for e in sys.stdin.readline().split()]

    min_cost = X * A + Y * B
    Z = 0
    while X > 0 or Y > 0:
        X = max(X - 1, 0)
        Y = max(Y - 1, 0)
        Z += 2
        cost = X * A + Y * B + Z * C
        min_cost = min(min_cost, cost)

    print(min_cost)


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
        input = """1500 2000 1600 3 2"""
        output = """7900"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1500 2000 1900 3 2"""
        output = """8500"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1500 2000 500 90000 100000"""
        output = """100000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
