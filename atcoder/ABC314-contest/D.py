import sys  # https://docs.python.org/ja/3/library/sys.html


def lower(N, S, M, Q):
    S = list(S)
    last = -1
    for i in reversed(range(M)):
        q = Q[i]
        if q[0] == "2" or q[0] == "3":
            last = i
            break

    for i, q in enumerate(Q):
        t, x, c = q
        if i == last:
            if t == "2":
                S = [s.lower() for s in S]
            elif t == "3":
                S = [s.upper() for s in S]
        else:
            if t == "1":
                S[int(x) - 1] = c

    return "".join(S)


def resolve():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    M = int(sys.stdin.readline())
    Q = [sys.stdin.readline().split() for _ in range(M)]
    print(lower(N, S, M, Q))


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
        input = """7
AtCoder
3
1 4 i
1 5 b
1 4 Y"""
        output = """AtCYber"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """7
AtCoder
5
1 4 i
3 0 a
1 5 b
2 0 a
1 4 Y"""
        output = """atcYber"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """35
TheQuickBrownFoxJumpsOverTheLazyDog
10
2 0 a
1 19 G
1 13 m
1 2 E
1 21 F
2 0 a
1 27 b
3 0 a
3 0 a
1 15 i"""
        output = """TEEQUICKBROWMFiXJUGPFOVERTBELAZYDOG"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
