import math


def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    total = 3**N
    odd_only = math.prod([2 if a % 2 == 0 else 1 for a in A])
    print(total - odd_only)


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
        input = """2
2 3"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
3 3 3"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
100"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
90 52 56 71 44 8 13 30 57 84"""
        output = """58921"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
