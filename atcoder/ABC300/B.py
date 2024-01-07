def resolve():
    def shift(row, t):
        return row[t:] + row[:t]

    def search(H, W, A, B):
        for s in range(H):
            for t in range(W):
                for u in range(H):
                    row = shift(A[(s + u) % H], t)
                    if row != B[u]:
                        break
                else:
                    return True
        return False
    
    H, W = [int(e) for e in input().split()]
    A = [input() for _ in range(H)]
    B = [input() for _ in range(H)]

    print("Yes" if search(H, W, A, B) else "No")


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
        input = """4 3
..#
...
.#.
...
#..
...
.#.
..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
##
##
#.
..
#.
#."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
#####
.#...
.##..
..##.
...##
#...#
#####
...#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 30
..........##########..........
..........####....###.....##..
.....##....##......##...#####.
....####...##..#####...##...##
...##..##..##......##..##....#
#.##....##....##...##..##.....
..##....##.##..#####...##...##
..###..###..............##.##.
.#..####..#..............###..
#..........##.................
................#..........##.
######....................####
....###.....##............####
.....##...#####......##....##.
.#####...##...##....####...##.
.....##..##....#...##..##..##.
##...##..##.....#.##....##....
.#####...##...##..##....##.##.
..........##.##...###..###....
...........###...#..####..#..."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
