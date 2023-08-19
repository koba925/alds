import sys

def row_compression(A):
    B = []
    for row in A:
        if "#" in row:
            B.append(row)
    return B

def grid_compression(H, W, A):
    B = zip(*row_compression(A))
    C = zip(*row_compression(B))
    return ["".join(row) for row in C]

def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    A = [sys.stdin.readline().strip() for _ in range(H)]

    print(*grid_compression(H, W, A), sep="\n")

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
        input = """4 4
##.#
....
##.#
.#.#"""
        output = """###
###
.##"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
#..
.#.
..#"""
        output = """#..
.#.
..#"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
.....
.....
..#..
....."""
        output = """#"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 6
......
....#.
.#....
..#...
..#...
......
.#..#."""
        output = """..#
#..
.#.
.#.
#.#"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
