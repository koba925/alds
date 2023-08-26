# https://atcoder.jp/contests/abc091/tasks/arc092_a
# TYPICAL90 27の類題 Mapで解く
# TODO: ソース確認
# TODO: 二部グラフの最大マッチング問題として考え、最大流アルゴリズムで解く

import sys


def ABC091(N, reds, blues):
    blues.sort()
    rused = [False] * N
    count = 0

    for bi, (bx, by) in enumerate(blues):
        maxri, maxry = -1, -1
        for ri, (rx, ry) in enumerate(reds):
            if rused[ri]:
                continue
            if rx < bx and ry < by and maxry < ry:
                maxry = ry
                maxri = ri
        if maxri != -1:
            rused[maxri] = True
            count += 1

    return count


def resolve():
    N = int(sys.stdin.readline())
    reds = [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    blues = [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    print(ABC091(N, reds, blues))


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
        input = """3
2 0
3 1
1 3
4 2
0 4
5 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
0 0
1 1
5 2
2 3
3 4
4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
2 2
3 3
0 0
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5
0 0
7 3
2 2
4 8
1 6
8 5
6 9
5 4
9 1
3 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """5
0 0
1 1
5 5
6 6
7 7
2 2
3 3
4 4
8 8
9 9"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
