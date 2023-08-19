import sys

def favorite_game(N, M, A):
    lower_start, upper_start = A[0], A[1]
    B = sorted(A[2:])

    min_move = float("inf")
    for left in range(len(B) - M + 1):
        right = left + M - 1
        lower = B[left]
        upper = B[right]
        move = 0
        if lower < lower_start:
            move += lower_start - lower
        if upper_start < upper:
            move += upper - upper_start
        min_move = min(min_move, move)

    return min_move

def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    print(favorite_game(N, M, A))

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

    def _test_入力例_1(self):
        input = """3 1
2 3 5"""
        output = """2"""
        self.assertIO(input, output)

    def _test_入力例_2(self):
        input = """5 2
1 4 2 3 5"""
        output = """0"""
        self.assertIO(input, output)

    def _test_入力例_3(self):
        input = """8 5
15 59 64 96 31 17 88 9"""
        output = """35"""
        self.assertIO(input, output)

    def test_00(self):
        input = """4 2
1000000000 1 1 1000000000"""
        output = """1999999998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
