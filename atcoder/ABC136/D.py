# D - Gathering Children
# TK: ランレングス圧縮、DP、ダブリング


def solve_tle(s):
    nums = [1] * len(s)
    prev_nums = None
    prev_prev_nums = None
    even_times = True
    while nums != prev_nums and nums != prev_prev_nums:
        new_nums = [0] * len(s)
        for i, dir in enumerate(s):
            if dir == "R":
                new_nums[i + 1] += nums[i]
            else:
                new_nums[i - 1] += nums[i]
        prev_prev_nums = prev_nums
        prev_nums = nums
        nums = new_nums
        even_times = not even_times
    return nums if even_times else prev_nums


def solve_editorial(s):
    n_boxes = len(s)
    s += "R"  # centinel

    ans = [0] * n_boxes
    left = right = 0
    while right < n_boxes:
        border = s.find("L", left)
        right = s.find("R", border)
        n_RL = right - left
        ans[border - 1] = ans[border] = n_RL // 2
        if n_RL % 2 == 1:
            ans[border - 1 + (right - border) % 2] += 1
        left = right

    return ans


def solve_dp(s):
    n_boxes = len(s)
    dp = [[0] * n_boxes for _ in range(33)]

    for i in range(n_boxes):
        dp[0][i] = i + 1 if s[i] == "R" else i - 1

    for p in range(32):
        for i in range(n_boxes):
            dp[p + 1][i] = dp[p][dp[p][i]]

    ans = [0] * n_boxes
    for i in range(n_boxes):
        ans[dp[32][i]] += 1

    return ans


def run_length(seq):
    length = len(seq)
    i, ret = 0, []
    while i < length:
        elem, count = seq[i], 0
        while i + count < length and seq[i + count] == elem:
            count += 1
        ret.append((elem, count))
        i += count
    return ret


def solve_runlength(s):
    ans = [0] * len(s)
    rl = run_length(s)
    pos = 0
    for i in range(0, len(rl), 2):
        r, l = rl[i][1], rl[i + 1][1]
        pos += r
        ans[pos - 1] = ans[pos] = (r + l) // 2
        if (r + l) % 2 == 1:
            ans[pos - l % 2] += 1
        pos += l
    return ans


def resolve():
    print(*solve_dp(input()))


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
        input = """RRLRL"""
        output = """0 1 2 1 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """RRLLLLRLRRLL"""
        output = """0 3 3 0 0 0 1 1 0 2 2 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """RRRLLRLLRRRLLLLL"""
        output = """0 0 3 2 0 2 1 0 0 0 4 4 0 0 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
