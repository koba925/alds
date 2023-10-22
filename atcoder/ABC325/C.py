def resolve():
    import collections as cl
    
    def bfs(sr, sc):
        q = cl.deque()
        q.append((sr, sc))
        visited[sr][sc] = True
        while q:
            qr, qc = q.popleft()
            for dr, dc in moves:
                r, c = qr + dr, qc + dc
                if 0 <= r < H and 0 <= c < W and S[r][c] == "#" and not visited[r][c]:
                    visited[r][c] = True
                    q.append((r, c))

    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]

    moves = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    visited = [[False] * W for _ in range(H)]
    count = 0

    for r in range(H):
        for c in range(W):
            if S[r][c] == "#" and not visited[r][c]:
                count += 1
                bfs(r, c)

    print(count)

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
        input = """5 6
.##...
...#..
....##
#.#...
..#..."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
#.#
.#.
#.#"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 2
..
..
..
.."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 47
.#..#..#####..#...#..#####..#...#...###...#####
.#.#...#.......#.#...#......##..#..#...#..#....
.##....#####....#....#####..#.#.#..#......#####
.#.#...#........#....#......#..##..#...#..#....
.#..#..#####....#....#####..#...#...###...#####"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
