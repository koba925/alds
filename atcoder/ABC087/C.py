import sys


def resolve_naive():
    N = int(sys.stdin.readline())
    A1 = [int(e) for e in sys.stdin.readline().split()]
    A2 = [int(e) for e in sys.stdin.readline().split()]
    max_candies = -1
    for i in range(0, N):
        candies = 0
        for j in range(0, N):
            if j <= i:
                candies += A1[j]
            if i <= j:
                candies += A2[j]
        max_candies = max(max_candies, candies)
    print(max_candies)


import itertools as it


def resolve():
    N = int(sys.stdin.readline())
    A1 = list(it.accumulate([int(e) for e in sys.stdin.readline().split()], initial=0))
    A2 = list(it.accumulate([int(e) for e in sys.stdin.readline().split()], initial=0))
    print(max(A1[i] + A2[N] - A2[i - 1] for i in range(1, N + 1)))


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
        input = """5
3 2 2 4 1
1 2 2 2 1"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
1 1 1 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
3 3 4 5 4 5 3
5 3 4 4 2 3 2"""
        output = """29"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
2
3"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
