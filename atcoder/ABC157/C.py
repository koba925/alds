import sys


def guess(N, M, SC):
    D = [None] + [-1] * N
    for s, c in SC:
        if D[s] != -1 and D[s] != c:
            return -1
        D[s] = c
    ans = ""
    for i, d in enumerate(D[1:], 1):
        if N > 1 and i == 1:
            if d == 0:
                return -1
            if d == -1:
                ans += "1"
            else:
                ans += str(d)
        else:
            if d == -1:
                ans += "0"
            else:
                ans += str(d)
    return ans


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    SC = [[int(e) for e in sys.stdin.readline().split()] for _ in range(M)]

    print(guess(N, M, SC))


def guess(N, M, SC):
    for n in range(0, 1000):
        ns = str(n)
        if len(ns) != N:
            continue
        for s, c in SC:
            if int(ns[s - 1]) != c:
                break
        else:
            return n
    return -1


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    SC = [[int(e) for e in sys.stdin.readline().split()] for _ in range(M)]

    print(guess(N, M, SC))


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
        input = """1 1
1 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_2(self):
        input = """3 0"""
        output = """100"""
        self.assertIO(input, output)

    def test_3(self):
        input = """1 0"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
