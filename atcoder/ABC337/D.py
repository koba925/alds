def resolve_TLE():
    H, W, K = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]

    def vertical(S, H, K, col):
        minop = K + 1
        for top in range(H - K + 1):
            op = K
            for i in range(K):
                if S[top + i][col] == "x": break
                if S[top + i][col] == "o": op -= 1
            else:
                minop = min(minop, op)
        return minop

    def horizontal(S, W, K, row):
        minop = K + 1
        for left in range(W - K + 1):
            op = K
            for i in range(K):
                if S[row][left + i] == "x": break
                if S[row][left + i] == "o": op -= 1
            else:
                minop = min(minop, op)
        return minop

    ans = K + 1
    for col in range(W):
        ans = min(ans, vertical(S, H, K, col))
    for row in range(H):
        ans = min(ans, horizontal(S, W, K, row))
    print(ans if ans <= K else -1)

def resolve():
    import itertools as it

    H, W, K = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]

    def gomoku(cells, l):
        minops = l + 1
        xs = [1 if cell == "x" else 0 for cell in cells]
        ps = [1 if cells == "." else 0 for cells in cells]
        xa = list(it.accumulate(xs, initial=0))
        pa = list(it.accumulate(ps, initial=0))
        for i in range(len(cells) - l + 1):
            nx = xa[i + l] - xa[i]
            np = pa[i + l] - pa[i]
            if nx == 0: minops = min(minops, np)
        return minops

    ans = K + 1
    for row in range(H):
        ans = min(ans, gomoku(S[row], K))
    for col in range(W):
        ans = min(ans, gomoku([s[col] for s in S], K))
    print(ans if ans <= K else -1)


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
        input = """3 4 3
xo.x
..o.
xx.o"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 2 3
.o
.o
.o
.o"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3 3
x..
..x
.x."""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 12 6
......xo.o..
x...x.....o.
x...........
..o...x.....
.....oo.....
o.........x.
ox.oox.xx..x
....o...oox.
..o.....x.x.
...o........"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
