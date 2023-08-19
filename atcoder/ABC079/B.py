import sys  # https://docs.python.org/ja/3/library/sys.html
import functools as ft  # https://docs.python.org/ja/3/library/functools.html


def lucas(N):
    l = [2, 1] + [None] * 85
    if N == 1:
        return 1
    for i in range(2, N + 1):
        l[i] = l[i - 1] + l[i - 2]
    return l[N]


@ft.lru_cache
def lucas_rec(N):
    return 2 if N == 0 else 1 if N == 1 else lucas_rec(N - 1) + lucas_rec(N - 2)


def resolve():
    N = int(sys.stdin.readline())
    print(lucas_rec(N))


# resolve()
# exit()

import sys
import unittest
from io import StringIO


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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
