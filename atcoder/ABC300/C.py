def resolve():
    def solve(H, W, S):
        def size_x(r, c):
            s = 0
            while S[r + s][c + s] == "#":
                S[r + s][c + s] = "."
                s += 1
            t = 0
            while t < s:
                S[r + t][c + s - 1 - t] = "."
                t += 1
            return (s - 1) // 2
        
        ans = [0] * min(H, W)
        for r in range(1, H + 1):
            for c in range(1, W + 1):
                if S[r][c] == "#":
                    ans[size_x(r, c) - 1] += 1
        return ans
        
    
    H, W = [int(e) for e in input().split()]
    S = [["."] * (W + 2)]
    for row in range(H):
        S.append(list("." + input() + "."))
    S.append(["."] * (W + 2))

    print(*solve(H, W, S))

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
        input = """5 9
#.#.#...#
.#...#.#.
#.#...#..
.....#.#.
....#...#"""
        output = """1 1 0 0 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
...
...
..."""
        output = """0 0 0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 16
#.#.....#.#..#.#
.#.......#....#.
#.#.....#.#..#.#"""
        output = """3 0 0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """15 20
#.#..#.............#
.#....#....#.#....#.
#.#....#....#....#..
........#..#.#..#...
#.....#..#.....#....
.#...#....#...#..#.#
..#.#......#.#....#.
...#........#....#.#
..#.#......#.#......
.#...#....#...#.....
#.....#..#.....#....
........#.......#...
#.#....#....#.#..#..
.#....#......#....#.
#.#..#......#.#....#"""
        output = """5 0 1 0 0 0 1 0 0 0 0 0 0 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
