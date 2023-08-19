# LL: 1-basedな累積和は0から取り始める
# TK: 累積和

import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    N = int(sys.stdin.readline())
    CP = [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    A = [[0] + [p if c == cl else 0 for c, p in CP] for cl in (1, 2)]
    for i in range(1, N + 1):
        A[0][i] += A[0][i - 1]
        A[1][i] += A[1][i - 1]

    Q = int(sys.stdin.readline())
    for _ in range(Q):
        l, r = [int(e) for e in sys.stdin.readline().split()]
        print(A[0][r] - A[0][l - 1], A[1][r] - A[1][l - 1])


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
        input = """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
1
2 6"""
        output = """63 261"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
1 72
2 78
2 94
1 23
2 89
1 40
1 75
10
1 3
2 4
3 5
4 6
5 7
1 5
2 6
3 7
1 6
2 7"""
        output = """72 172
23 172
23 183
63 89
115 89
95 261
63 261
138 183
135 261
138 261"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1 100
3
1 1
1 1
1 1"""
        output = """100 0
100 0
100 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20
2 90
1 67
2 9
2 17
2 85
2 43
2 11
1 32
2 16
1 19
2 65
1 14
1 51
2 94
1 4
1 55
2 90
1 89
1 35
2 81
20
3 17
5 5
11 11
8 10
3 13
2 6
3 7
3 5
12 18
4 8
3 16
6 8
3 20
1 12
1 6
5 16
3 10
17 19
4 4
7 15"""
        output = """175 430
0 85
0 65
51 16
116 246
67 154
0 165
0 111
213 184
32 156
175 340
32 54
299 511
132 336
67 244
175 314
51 181
124 90
0 17
120 186"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

# def score_sum_queries(N, S, C, L, R):
#     return S[C][R] - S[C][L - 1]

# def resolve():
#     N = int(sys.stdin.readline())
#     S = [None] + [[0] + [0] * N, [0] + [0] * N]
#     for i in range(1, N + 1):
#         c, p = [int(e) for e in sys.stdin.readline().split()]
#         S[c][i] = p
#     for i in range(2, N + 1):
#         S[1][i] += S[1][i - 1]
#         S[2][i] += S[2][i - 1]

#     Q = int(sys.stdin.readline())
#     for _ in range(Q):
#         L, R = [int(e) for e in sys.stdin.readline().split()]
#         print(score_sum_queries(N, S, 1, L, R), score_sum_queries(N, S, 2, L, R))
