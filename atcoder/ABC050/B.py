import sys  # https://docs.python.org/ja/3/library/sys.html


def contest_naive(N, T, M, PX):
    ans = []

    for i in range(M):
        p, x = PX[i]
        s = 0
        for j in range(N):
            s += x if j == p - 1 else T[j]
        ans.append(s)

    return ans


def contest_difference(N, T, M, PX):
    total = sum(T)
    ans = []
    for p, x in PX:
        ans.append(total - T[p - 1] + x)
    return ans


def contest(N, T, M, PX):
    total = sum(T)
    return [total - T[p - 1] + x for p, x in PX]


def resolve():
    N = int(sys.stdin.readline())
    T = [int(e) for e in sys.stdin.readline().split()]
    M = int(sys.stdin.readline())
    PX = [[int(e) for e in sys.stdin.readline().split()] for _ in range(M)]
    print(*contest(N, T, M, PX), sep="\n")


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
        input = """3
2 1 4
2
1 1
2 3"""
        output = """6
9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
7 2 3 8 5
3
4 2
1 7
4 13"""
        output = """19
25
30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
