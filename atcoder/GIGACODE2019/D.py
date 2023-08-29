# TK: 2次元累積和

import sys


# 2次元累積和
def cumulative_sum_2D(H, W, A):
    S = [[0] * (W + 1) for _ in range(H + 1)]
    for r in range(H):
        for c in range(W):
            S[r + 1][c + 1] = S[r][c + 1] + S[r + 1][c] - S[r][c] + A[r][c]
    return S


# 長方形(r1, c1)-(r2, c2)の和（r2,c2)を含む
def get_sum_2D(S, r1, c1, r2, c2):
    return S[r2 + 1][c2 + 1] - S[r1][c2 + 1] - S[r2 + 1][c1] + S[r1][c1]


def resolve():
    H, W, K, V = [int(e) for e in sys.stdin.readline().split()]
    A = [[int(e) for e in sys.stdin.readline().split()] for _ in range(H)]
    S = cumulative_sum_2D(H, W, A)

    ret = 0
    for r1 in range(H):
        for r2 in range(r1, H):
            rd = r2 - r1 + 1
            for c1 in range(W):
                for c2 in range(c1, W):
                    cd = c2 - c1 + 1
                    if get_sum_2D(S, r1, c1, r2, c2) + rd * cd * K <= V:
                        ret = max(ret, rd * cd)

    print(ret)


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
        input = """1 1 200 500
300"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 8 10 200
30 40 10 20 30 40 10 20"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5 10 17
12 19 25 13 25
14 16 18 11 10
19 17 24 26 12
23 11 16 19 14
18 23 27 11 16"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 7 10 240
17 12 15 18 19 15 23
22 12 41 16 27 10 10
15 69 18 11 10 23 15
12 20 13 12 17 18 15"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
