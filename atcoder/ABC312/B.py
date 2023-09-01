import sys


def tak_code(N, M, S):
    def is_tak(top, left):
        for r in range(3):
            for c in range(3):
                if S[top + r][left + c] == ".":
                    return False
        for r in range(6, 9):
            for c in range(6, 9):
                if S[top + r][left + c] == ".":
                    return False
        for r in range(4):
            if S[top + r][left + 3] == "#":
                return False
        for r in range(5, 9):
            if S[top + r][left + 5] == "#":
                return False
        for c in range(4):
            if S[top + 3][left + c] == "#":
                return False
        for c in range(5, 9):
            if S[top + 5][left + c] == "#":
                return False
        return True

    for top in range(N - 8):
        for left in range(M - 8):
            if is_tak(top, left):
                print(top + 1, left + 1)


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    S = [list(sys.stdin.readline().strip()) for _ in range(N)]
    tak_code(N, M, S)


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

    def test_(self):
        input = """9 9
###......
###......
###......
.........
.........
.........
......###
......###
......###
"""
        output = """1 1"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """19 18
###......###......
###......###......
###..#...###..#...
..............#...
..................
..................
......###......###
......###......###
......###......###
.###..............
.###......##......
.###..............
............###...
...##.......###...
...##.......###...
.......###........
.......###........
.......###........
........#........."""
        output = """1 1
1 10
7 7
10 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 21
###.#...........#.###
###.#...........#.###
###.#...........#.###
....#...........#....
#########...#########
....#...........#....
....#.###...###.#....
....#.###...###.#....
....#.###...###.#...."""
        output = """1 1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """18 18
######............
######............
######............
######............
######............
######............
..................
..................
..................
..................
..................
..................
............######
............######
............######
............######
............######
............######"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
