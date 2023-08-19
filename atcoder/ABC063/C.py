import sys  # https://docs.python.org/ja/3/library/sys.html


def bugged_normal(N, S):
    total = sum(S)
    if total % 10 != 0:
        return total
    s = [s for s in sorted(S) if s % 10 != 0]
    return total - s[0] if s else 0


def bugged_dp_overkill(N, S):
    MAX_SCORE = sum(S)
    scores = [True] + [False] * (MAX_SCORE)
    next = [None] * (MAX_SCORE + 1)
    for s in S:
        for t in range(MAX_SCORE + 1):
            next[t] = scores[t] or scores[t - s]
        scores = next
        next = [None] * (MAX_SCORE + 1)
    scores = [
        s for s, b in sorted(enumerate(scores), reverse=True) if b and s % 10 != 0
    ]
    return scores[0] if scores else 0


def resolve():
    N = int(sys.stdin.readline())
    S = [int(sys.stdin.readline()) for _ in range(N)]
    print(bugged_dp_overkill(N, S))


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

    def test_1(self):
        input = """4
1
2
3
4"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3
5
10
15"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
10
10
15"""
        output = """35"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
10
20
30"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
