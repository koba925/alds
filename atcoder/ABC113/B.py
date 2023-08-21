# LL: 10**n倍して整数化

import sys  # https://docs.python.org/ja/3/library/sys.html


def palace_mine(N, T, A, H):
    min_diff = 10**9
    for i in range(N):
        diff = abs(A - (T - H[i] * 0.006))
        if diff < min_diff:
            palace_num = i + 1
            min_diff = diff
    return palace_num


def palace(N, T, A, H):
    min_diff = 10**9
    for i in range(N):
        diff = abs(A * 1000 - (T * 1000 - H[i] * 6))
        if diff < min_diff:
            palace_num = i + 1
            min_diff = diff
    return palace_num


def resolve():
    N = int(sys.stdin.readline())
    T, A = [int(e) for e in sys.stdin.readline().split()]
    H = [int(e) for e in sys.stdin.readline().split()]
    print(palace(N, T, A, H))


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
12 5
1000 2000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
21 -11
81234 94124 52141"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
