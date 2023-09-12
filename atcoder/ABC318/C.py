import sys


def resolve_contest():
    N, D, P = [int(e) for e in sys.stdin.readline().split()]
    F = [int(e) for e in sys.stdin.readline().split()]
    F.sort(reverse=True)

    min_fee = fee = sum(F)
    for p in range(N // D + 1):
        fee = fee - sum(F[p * D : (p + 1) * D]) + P
        min_fee = min(min_fee, fee)
    print(min_fee)


def resolve():
    N, D, P = [int(e) for e in sys.stdin.readline().split()]
    F = [0] + [int(e) for e in sys.stdin.readline().split()]

    F.sort()
    for i in range(1, N + 1):
        F[i] += F[i - 1]

    min_fee = float("inf")
    for p in range(N // D + 2):
        min_fee = min(min_fee, F[max(0, N - p * D)] + p * P)

    print(min_fee)


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
        input = """5 2 10
7 1 6 3 6"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 10
1 2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 3 1000000000
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """3000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
