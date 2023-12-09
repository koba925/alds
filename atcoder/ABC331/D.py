def resolve():
    def cumulative_sum_2D(H, W, A):
        S = [[0] * (W + 1) for _ in range(H + 1)]
        for r in range(H):
            for c in range(W):
                S[r + 1][c + 1] = S[r][c + 1] + S[r + 1][c] - S[r][c] + A[r][c]
        return S

    def get_sum_2D(r1, c1, r2, c2):
        return S[r2 + 1][c2 + 1] - S[r1][c2 + 1] - S[r2 + 1][c1] + S[r1][c1]

    def get_sum_2D_half_open(r1, c1, r2, c2):
        return S[r2][c2] - S[r1][c2] - S[r2][c1] + S[r1][c1]

    def solve_contest(S, A, B, C, D):
        m_t = A % N
        m_l = B % N
        m_b = C % N
        m_r = D % N
        n_v = C // N - A // N - 1
        n_h = D // N - B // N - 1

        tl = get_sum_2D(m_t, m_l, N - 1, N - 1)
        tr = get_sum_2D(m_t, 0, N - 1, m_r)
        bl = get_sum_2D(0, m_l, m_b, N - 1)
        br = get_sum_2D(0, 0, m_b, m_r)

        a_l = n_v * get_sum_2D(0, m_l, N - 1, N - 1)
        a_r = n_v * get_sum_2D(0, 0, N - 1, m_r)
        a_t = n_h * get_sum_2D(m_t, 0, N - 1, N - 1)
        a_b = n_h * get_sum_2D(0, 0, m_b, N - 1)
        a_c = n_v * n_h * get_sum_2D(0, 0, N - 1, N - 1)

        return tl + tr + bl + br + a_l + a_r + a_t + a_b + a_c

    def solve_editorial(S, A, B, C, D):
        def from_o(A, B):
            n_v, n_h = A // N, B // N
            m_b, m_r = A % N, B % N

            b_tl = n_v * n_h * get_sum_2D_half_open(0, 0, N, N)
            b_tr = n_v * get_sum_2D_half_open(0, 0, N, m_r)
            b_bl = n_h * get_sum_2D_half_open(0, 0, m_b, N)
            b_br = get_sum_2D_half_open(0, 0, m_b, m_r)

            return b_tl + b_tr + b_bl + b_br

        return from_o(C + 1, D + 1) + from_o(A, B) - from_o(A, D + 1) - from_o(C + 1, B)

    N, Q = [int(e) for e in input().split()]
    P = [[1 if p == "B" else 0 for p in input()] for _ in range(N)]

    S = cumulative_sum_2D(N, N, P)

    for _ in range(Q):
        A, B, C, D = [int(e) for e in input().split()]
        print(solve_editorial(S, A, B, C, D))


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
        input = """3 3
WWB
BBW
WBW
1 2 3 4
0 3 4 5
1 2 2 2
"""
        output = """4
7
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 5
BBBWWWBBBW
WWWWWBBBWB
BBBWBBWBBB
BBBWWBWWWW
WWWWBWBWBW
WBBWBWBBBB
WWBBBWWBWB
WBWBWWBBBB
WBWBWBBWWW
WWWBWWBWWB
5 21 21 93
35 35 70 43
55 72 61 84
36 33 46 95
0 0 999999999 999999999"""
        output = """621
167
44
344
500000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
