# https://atcoder.jp/contests/gigacode-2019/tasks/gigacode_2019_d
# https://atcoder.jp/contests/abc331/tasks/abc331_d

# r, c は 0-based

# 2次元累積和
# S[0][c] や S[r][0]は0

def cumulative_sum_2D(H, W, A):
    S = [[0] * (W + 1) for _ in range(H + 1)]
    for r in range(H):
        for c in range(W):
            S[r + 1][c + 1] = S[r][c + 1] + S[r + 1][c] - S[r][c] + A[r][c]
    return S

# 長方形(r1, c1)-(r2, c2)の和（r2,c2)を含む
def get_sum_2D(S, r1, c1, r2, c2):
    return S[r2 + 1][c2 + 1] - S[r1][c2 + 1] - S[r2 + 1][c1] + S[r1][c1]

# 長方形(r1, c1)-(r2, c2)の和 r2行、c2列を含まない → 高さ0、幅0も計算可能
def get_sum_2D_half_open(S, r1, c1, r2, c2):
    return S[r2][c2] - S[r1][c2] - S[r2][c1] + S[r1][c1]

import unittest

class TestClass(unittest.TestCase):
    def calc_sum(self, r1, c1, r2, c2, f):
        A = [[1, 2, 1, 2],
             [2, 1, 2, 1],
             [1, 2, 1, 2]]
        S = cumulative_sum_2D(3, 4, A)
        return f(S, r1, c1, r2, c2)

    def test_top_left(self):
        self.assertEqual(self.calc_sum(0, 0, 0, 0, get_sum_2D), 1)

    def test_bottom_right(self):
        self.assertEqual(self.calc_sum(2, 3, 2, 3, get_sum_2D), 2)

    def test_whole(self):
        self.assertEqual(self.calc_sum(0, 0, 2, 3, get_sum_2D), 18)

    def test_middle(self):
        self.assertEqual(self.calc_sum(1, 1, 1, 2, get_sum_2D), 3)

    def test_top_left_half_open(self):
        self.assertEqual(self.calc_sum(0, 0, 1, 1, get_sum_2D_half_open), 1)

    def test_bottom_right_half_open(self):
        self.assertEqual(self.calc_sum(2, 3, 3, 4, get_sum_2D_half_open), 2)

    def test_whole_half_open(self):
        self.assertEqual(self.calc_sum(0, 0, 3, 4, get_sum_2D_half_open), 18)

    def test_middle_half_open(self):
        self.assertEqual(self.calc_sum(1, 1, 2, 3, get_sum_2D_half_open), 3)

    def test_zero_width_half_open(self):
        self.assertEqual(self.calc_sum(1, 2, 3, 2, get_sum_2D_half_open), 0)

    def test_zero_height_half_open(self):
        self.assertEqual(self.calc_sum(0, 1, 0, 3, get_sum_2D_half_open), 0)


    def test_zero_area_half_open(self):
        self.assertEqual(self.calc_sum(1, 1, 1, 1, get_sum_2D_half_open), 0)

unittest.main()