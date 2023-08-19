# LL: 余事象を考える
# TK: ランレングス圧縮

import sys  # https://docs.python.org/ja/3/library/sys.html


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


def sum_to(n):
    return n * (n + 1) // 2


def twotype_runlength(N: int, S: str) -> int:
    return sum_to(N) - sum(sum_to(n) for _, n in run_length(S))


def twotype_dp(N: int, S: str) -> int:
    S = " " + S
    last_o, last_x = [0] * (N + 1), [0] * (N + 1)
    for i in range(1, N + 1):
        last_o[i] = i if S[i] == "o" else last_o[i - 1]
        last_x[i] = i if S[i] == "x" else last_x[i - 1]

    # ans = 0
    # for i in range(1, N + 1):
    #     ans += min(last_o[i], last_x[i])
    # return ans

    return sum(min(o, x) for o, x in zip(last_o, last_x))


def resolve():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    print(twotype_dp(N, S))


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
        input = """4
ooxo"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
oxoxo"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
ooooo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7
xxoooxx"""
        output = """16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
