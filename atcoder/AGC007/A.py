def resolve():
    def dfs(A, r, c):
        if (r, c) == (H - 1, W - 1):
            return all(all(a == "." for a in row) for row in A)
        
        if r + 1 < H and A[r + 1][c] == "#":
            A[r + 1][c] = "."
            res = dfs(A, r + 1, c)
            if res: return True
            A[r + 1][c] = "#"
        if c + 1 < W and A[r][c + 1] == "#":
            A[r][c + 1] = "."
            res = dfs(A, r, c + 1)
            if res: return True
            A[r][c + 1] = "#"
        return False

    H, W = [int(e) for e in input().split()]
    A = [list(input()) for _ in range(H)]
    A[0][0] = "."
    print("Possible" if dfs(A, 0, 0) else "Impossible")

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
        input = """4 5
##...
.##..
..##.
...##"""
        output = """Possible"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 3
###
..#
###
#..
###"""
        output = """Impossible"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 5
##...
.###.
.###.
...##"""
        output = """Impossible"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
