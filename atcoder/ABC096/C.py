import sys

def grid_repainting_2(H, W, S):
    def black_neighbors(r, c):
        for delta in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            nr = r + delta[0]
            nc = c + delta[1]
            if 0 <= nr < H and 0 <= nc < W and S[nr][nc] == "#":
                return True
        return False

    for r in range(H):
        for w in range(W):
            if S[r][w] == "#" and not black_neighbors(r, w):
                return False
    return True

def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    S = [list(sys.stdin.readline().strip()) for _ in range(H)]    
    print("Yes" if grid_repainting_2(H, W, S) else "No")

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
        input = """3 3
.#.
###
.#."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
#.#.#
.#.#.
#.#.#
.#.#.
#.#.#"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 11
...#####...
.##.....##.
#..##.##..#
#..##.##..#
#.........#
#...###...#
.#########.
.#.#.#.#.#.
##.#.#.#.##
..##.#.##..
.##..#..##."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
