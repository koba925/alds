import sys
from io import StringIO
import unittest

def resolve_recursive():
    def solve(top, left, bottom, right):
        def find_two():
            strawberries = []
            for r in range(top, bottom):
                for c in range(left, right):
                    if S[r][c] == "#":
                        strawberries.append((r, c))
                        if len(strawberries) == 2:
                            return strawberries
            return []

        def paint():        
            for r in range(top, bottom):
                for c in range(left, right):
                    C[r][c] = k

        nonlocal C, k
        strawberries = find_two()
        if not strawberries:
            paint()
            k += 1
            return
        
        (r1, c1), (r2, c2) = strawberries
        if r1 != r2:
            solve(top, left, r1 + 1, right)
            solve(r1 + 1, left, bottom, right)
        else:
            solve(top, left, bottom, c1 + 1)
            solve(top, c1 + 1, bottom, right)

    H, W, K = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]

    C = [[0] * W for _ in range(H)]
    k = 1
    solve(0, 0, H, W)

    for row in C:
        print(*row)

def resolve_vertihoriz():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    H, W, K = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]

    C = [[0] * W for _ in range(H)]
    k = 1
    r1 = r2 = 0
    while S[r2].count("#") == 0:
        r2 += 1
    while r2 < H:
        r2 += 1
        while r2 < H and S[r2].count("#") == 0:
            r2 += 1
        c1 = c2 = 0
        while [S[r][c2] for r in range(r1, r2)].count("#") == 0:
            c2 += 1
        while c2 < W:
            c2 += 1
            while c2 < W and [S[r][c2] for r in range(r1, r2)].count("#") == 0:
                c2 += 1
            for r in range(r1, r2):
                for c in range(c1, c2):
                    C[r][c] = k
            k += 1
            c1 = c2
        r1 = r2

    for row in C:
        debug(*row)
        print(*row)


def resolve():
    H, W, K = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]
    C = [[0] * W for _ in range(H)]

    k = 1
    for r in range(H):
        for c in range(W):
            if S[r][c] == "#":
                C[r][c] = k
                k += 1

    for r in range(H):
        for c in range(1, W):
            if C[r][c] == 0:
                C[r][c] = C[r][c - 1]
        for c in reversed(range(W - 1)):
            if C[r][c] == 0:
                C[r][c] = C[r][c + 1]

    for c in range(W):
        for r in range(1, H):
            if C[r][c] == 0:
                C[r][c] = C[r - 1][c]
        for r in reversed(range(H - 1)):
            if C[r][c] == 0:
                C[r][c] = C[r + 1][c]

    for row in C:
        print(*row)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 3 5
#.#
.#.
#.#"""
        expected = """1 2 2
1 3 4
5 5 4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 7 7
#...#.#
..#...#
.#..#.."""
        expected = """1 1 2 2 3 4 4
6 6 2 2 3 5 5
6 6 7 7 7 7 7"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """13 21 106
.....................
.####.####.####.####.
..#.#..#.#.#....#....
..#.#..#.#.#....#....
..#.#..#.#.#....#....
.####.####.####.####.
.....................
.####.####.####.####.
....#.#..#....#.#..#.
.####.#..#.####.#..#.
.#....#..#.#....#..#.
.####.####.####.####.
....................."""
        expected = """12 12 23 34 45 45 60 71 82 93 93 2 13 24 35 35 17 28 39 50 50
12 12 23 34 45 45 60 71 82 93 93 2 13 24 35 35 17 28 39 50 50
12 12 56 89 89 89 60 104 82 31 31 46 13 24 35 35 61 61 39 50 50
12 12 67 67 100 100 60 9 9 42 42 57 13 24 6 72 72 72 72 72 72
12 12 78 5 5 5 20 20 20 53 68 68 90 24 6 83 83 83 83 83 83
16 16 27 38 49 49 64 75 86 97 79 79 90 101 6 94 94 105 10 21 21
16 16 27 38 49 49 64 75 86 97 79 79 90 101 6 94 94 105 10 21 21
32 32 43 54 65 65 80 11 106 95 22 22 33 44 55 55 70 1 96 85 85
32 32 43 54 76 76 91 11 106 84 84 4 99 66 66 66 81 1 96 74 74
14 14 3 98 87 87 102 11 73 73 73 4 99 88 77 77 92 92 63 63 63
25 25 3 98 87 87 7 29 62 62 62 15 99 88 77 77 103 19 30 52 52
36 36 47 58 69 69 18 29 40 51 51 26 37 48 59 59 8 19 30 41 41
36 36 47 58 69 69 18 29 40 51 51 26 37 48 59 59 8 19 30 41 41"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        # self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
