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
        return

    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]    
    print(range_flip())

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
