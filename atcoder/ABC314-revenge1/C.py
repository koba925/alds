import sys  # https://docs.python.org/ja/3/library/sys.html


def rotate_colored_subsequence(N, M, S, C):
    positions = [None] + [[] for _ in range(M)]
    for i, c in enumerate(C):
        positions[c].append(i)

    for c in range(1, M + 1):
        l = len(positions[c])
        temp = S[positions[c][-1]]
        for i in reversed(range(1, l)):
            S[positions[c][i]] = S[positions[c][i - 1]]
        S[positions[c][0]] = temp

    return S


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    S = list(sys.stdin.readline().strip())
    C = [int(e) for e in sys.stdin.readline().split()]
    print("".join(rotate_colored_subsequence(N, M, S, C)))


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
        input = """8 3
apzbqrcs
1 2 3 1 2 2 1 2"""
        output = """cszapqbr"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
aa
1 1"""
        output = """aa"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
