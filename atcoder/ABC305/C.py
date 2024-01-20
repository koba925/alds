def resolve():
    def cookie_picker(H, W, S):
        top, bottom, left, right = 501, -1, 501, -1

        for row, s in enumerate(S):
            if "#" not in s: continue
            if top == 501: top = row
            bottom = row
            left = min(left, s.find("#"))
            right = max(right, s.rfind("#"))

        for row in range(top, bottom + 1):
            for col in range(left, right + 1):
                if S[row][col] == ".":
                    return (row + 1, col + 1)

    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]
    print(*cookie_picker(H, W, S))

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
......
..#.#.
..###.
..###.
......"""
        output = """2 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
#.
##
##"""
        output = """1 2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 6
..####
..##.#
..####
..####
..####
......"""
        output = """2 5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
