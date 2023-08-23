# LL: 問題文を一字一句理解して読む

import sys  # https://docs.python.org/ja/3/library/sys.html


def travelling(N, TXY):
    curt, curx, cury = 0, 0, 0
    for t, x, y in TXY[1:]:
        dt, dx, dy = t - curt, x - curx, y - cury
        dist = abs(dx) + abs(dy)
        if dt < dist or (dist - dt) % 2 == 1:
            return False
        curt, curx, cury = t, x, y
    return True


def travelling(N, TXY):
    for i in range(N):
        (t, x, y), (nt, nx, ny) = TXY[i], TXY[i + 1]
        dt, dx, dy = nt - t, nx - x, ny - y
        dist = abs(dx) + abs(dy)
        if dt < dist or (dist - dt) % 2 == 1:
            return False
    return True


def resolve():
    N = int(sys.stdin.readline())
    TXY = [[0, 0, 0]] + [
        [int(e) for e in sys.stdin.readline().split()] for _ in range(N)
    ]
    print("Yes" if travelling(N, TXY) else "No")


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
        input = """2
3 1 2
5 1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """2
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
