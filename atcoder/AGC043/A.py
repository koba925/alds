def resolve_naivedfs_TLE():
    def range_flip():
        def dfs(r, c, prev, flips):
            nonlocal ans

            curr = S[r][c]
            if prev == "." and curr == "#": flips += 1

            if r == H - 1 and c == W - 1:
                ans = min(ans, flips)
                return

            if r < H - 1:
                dfs(r + 1, c, curr, flips)
            if c < W - 1:
                dfs(r, c + 1, curr, flips)

        ans = float("inf")
        dfs(0, 0, ".", 0)
        return ans

    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]
    print(range_flip())

def resolve():
    def range_flip():
        def dfs(r, c, flips):
            nonlocal ans

            if r == H - 1 and c == W - 1:
                ans = min(ans, flips)
                return

            curr = S[r][c]
            right = S[r + 1][c] if r < H - 1 else None
            down = S[r][c + 1] if c < W - 1 else None

            if right != curr and down != curr:
                if curr == ".": flips += 1
                if right: dfs(r + 1, c, flips)
                if down: dfs(r, c + 1, flips)
            else:
                if right == curr: dfs(r + 1, c, flips)
                if down == curr: dfs(r, c + 1, flips)

        ans = float("inf")
        dfs(0, 0, 1 if S[0][0] == "#" else 0)
        return ans

    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]
    print(range_flip())

def resolve():
    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]

    memo = [[1000] * W for _ in range(H)]
    memo[0][0] = 1 if S[0][0] == "#"  else 0
    for r in range(H):
        for c in range(W):
             if r > 0:
                memo[r][c] = min(memo[r][c], 
                     memo[r - 1][c] + (1 if S[r - 1][c] == "." and S[r][c] == "#" else 0)
                )   
             if c > 0:
                memo[r][c] = min(memo[r][c], 
                     memo[r][c - 1] + (1 if S[r][c - 1] == "." and S[r][c] == "#"  else 0)
                )   
    print(memo[H - 1][W - 1])

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
.##
.#.
##."""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2
#.
.#"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 4
..##
#...
###.
###."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 5
.#.#.
#.#.#
.#.#.
#.#.#
.#.#."""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
