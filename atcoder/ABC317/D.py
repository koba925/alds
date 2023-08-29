import sys


def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def resolve_2D():
    N = int(sys.stdin.readline())
    X, Y, Z = zip(*[[int(e) for e in sys.stdin.readline().split()] for _ in range(N)])
    total = sum(Z)
    border = total // 2 + 1
    # debug("\n", total, border)

    memo = [[float("inf")] * (total + 1) for _ in range(N + 1)]
    memo[N][0] = 0

    for i in reversed(range(N)):
        for j in reversed(range(total + 1)):
            memo[i][j] = memo[i + 1][j]
            w = max((Y[i] - X[i] + 1) // 2, 0)
            if j >= Z[i]:
                memo[i][j] = min(memo[i][j], memo[i + 1][j - Z[i]] + w)

    # debug("", *memo, sep="\n")
    print(min(memo[0][border:]))


def resolve():
    N = int(sys.stdin.readline())
    X, Y, Z = zip(*[[int(e) for e in sys.stdin.readline().split()] for _ in range(N)])
    total = sum(Z)
    border = total // 2 + 1
    # debug("\n", total, border)

    memo = [0] + [float("inf")] * total

    for i in reversed(range(N)):
        for j in reversed(range(total + 1)):
            w = max((Y[i] - X[i] + 1) // 2, 0)
            if j >= Z[i]:
                memo[j] = min(memo[j], memo[j - Z[i]] + w)
        # debug(memo)

    print(min(memo[border:]))


# resolve()
# resolve_2D()
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
        input = """3
10 21 30
5 2 8
15 18 3
"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """1
3 8 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3 6 2
1 8 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
3 4 2
1 2 3
7 2 6"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10
1878 2089 16
1982 1769 13
2148 1601 14
2189 2362 15
2268 2279 16
2394 2841 18
2926 2971 20
3091 2146 20
3878 4685 38
4504 4617 29"""
        output = """86"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
