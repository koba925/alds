def resolve():
    H, W = [int(e) for e in input().split()]
    N = int(input())
    A = [int(e) for e in input().split()]

    G = [[0] * W for _ in range(H)]
    row, col = 0, 0
    for color, a in enumerate(A, 1):
        for _ in range(a):
            G[row][col] = color
            col += 1 if row % 2 == 0 else -1
            if col < 0: row, col = row + 1, 0
            if W <= col: row, col = row + 1, W - 1

    for g in G: print(*g)

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
        input = """2 2
3
2 1 1"""
        output = """1 1
2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
5
1 2 3 4 5"""
        output = """1 4 4 4 3
2 5 4 5 3
2 5 5 5 3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
1
1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
