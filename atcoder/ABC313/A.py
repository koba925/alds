# LL: maxを使うときはiterableが空でないか気を付ける。default=が使える。

import sys


def to_be_saikyo_mine(N, P):
    if N == 1:
        return 0

    max_score = max(P[1:])
    if P[0] > max_score:
        return 0
    return max_score - P[0] + 1


def to_be_saikyo_editorial(N, P):
    return max(0, max(P[1:], default=0) - P[0] + 1)


def resolve():
    N = int(sys.stdin.readline())
    P = [int(e) for e in sys.stdin.readline().split()]
    print(to_be_saikyo_editorial(N, P))


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
        input = """1
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """4
5 15 2 10"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
15 5 2 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
100 100 100"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
