def resolve():
    H, W, N = [int(e) for e in input().split()]

    G = [["."] * W for _ in range(H)]
    dcol = [0, 1, 0, -1]
    drow = [-1, 0, 1, 0]
    dir = 0
    row, col = 0, 0
    for _ in range(N):
        if G[row][col] == ".":
            G[row][col] = "#"
            dir = (dir + 1) % 4
        else:
            G[row][col] = "."
            dir = (dir - 1) % 4
        row = (row + drow[dir]) % H
        col = (col + dcol[dir]) % W
    
    for row in range(H):
        print("".join(G[row]))

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
        input = """3 4 5"""
        output = """.#..
##..
...."""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2 1000"""
        output = """..
.."""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 10 10"""
        output = """##........
##........
..........
..........
..........
..........
..........
..........
..........
#........#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
