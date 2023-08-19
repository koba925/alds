import sys  # https://docs.python.org/ja/3/library/sys.html


def lamp(H, W, S):
    hbarrier = [[-1] for _ in range(H)]
    for r, row in enumerate(S):
        for c, s in enumerate(row):
            if s == "#":
                hbarrier[r].append(c)
        hbarrier[r].append(W)

    hspan = [[0] * W for _ in range(H)]
    for r in range(H):
        for i in range(len(hbarrier[r]) - 1):
            for c in range(hbarrier[r][i] + 1, hbarrier[r][i + 1]):
                hspan[r][c] = hbarrier[r][i + 1] - hbarrier[r][i] - 1

    wbarrier = [[-1] for _ in range(W)]
    for c, col in enumerate(zip(*S)):
        for r, s in enumerate(col):
            if s == "#":
                wbarrier[c].append(r)
        wbarrier[c].append(H)

    wspan = [[0] * W for _ in range(H)]
    for c in range(W):
        for i in range(len(wbarrier[c]) - 1):
            for r in range(wbarrier[c][i] + 1, wbarrier[c][i + 1]):
                wspan[r][c] = wbarrier[c][i + 1] - wbarrier[c][i] - 1

    max_light = 0
    for r in range(H):
        for c in range(W):
            if S[r][c] == ".":
                light = hspan[r][c] + wspan[r][c] - 1
                max_light = max(max_light, light)

    return max_light


def lamp_editorial1(H, W, S):
    L = [[0] * W for _ in range(H)]
    for r in range(H):
        length = 0
        for c in range(W):
            length = 0 if S[r][c] == "#" else length + 1
            L[r][c] = length

    R = [[0] * W for _ in range(H)]
    for r in range(H):
        length = 0
        for c in reversed(range(W)):
            length = 0 if S[r][c] == "#" else length + 1
            R[r][c] = length

    U = [[0] * W for _ in range(H)]
    for c in range(W):
        length = 0
        for r in range(H):
            length = 0 if S[r][c] == "#" else length + 1
            U[r][c] = length

    D = [[0] * W for _ in range(H)]
    for c in range(W):
        length = 0
        for r in reversed(range(H)):
            length = 0 if S[r][c] == "#" else length + 1
            D[r][c] = length

    max_light = 0
    for r in range(H):
        for c in range(W):
            if S[r][c] == ".":
                light = L[r][c] + R[r][c] + U[r][c] + D[r][c] - 3
                max_light = max(max_light, light)

    return max_light


from bisect import bisect


def lamp_editorial2(H, W, S):
    hbarrier = [[-1] for _ in range(H)]
    wbarrier = [[-1] for _ in range(W)]

    for r, row in enumerate(S):
        for c, s in enumerate(row):
            if s == "#":
                hbarrier[r].append(c)
                wbarrier[c].append(r)
        hbarrier[r].append(W)

    for c in range(len(S[0])):
        wbarrier[c].append(H)

    max_light = 0
    for r in range(H):
        for c in range(W):
            if S[r][c] == ".":
                ileft = bisect(hbarrier[r], c)
                hspan = hbarrier[r][ileft] - hbarrier[r][ileft - 1] - 1

                iupper = bisect(wbarrier[c], r)
                wspan = wbarrier[c][iupper] - wbarrier[c][iupper - 1] - 1

                max_light = max(max_light, hspan + wspan - 1)

    return max_light


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    S = [list(sys.stdin.readline().strip()) for _ in range(H)]
    print(lamp_editorial1(H, W, S))


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
        input = """4 6
#..#..
.....#
....#.
#.#..."""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 8
..#...#.
....#...
##......
..###..#
...#..#.
##....#.
#...#...
###.#..#"""
        output = """13"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
