import sys, math, itertools as it, functools as ft, collections as cl


def coloring(S, color):
    S = [int(e) for e in S]
    ret = 0
    for i, s in enumerate(S):
        if S[i] != color:
            ret += 1
        color = 1 - color
    return ret


def coloring(S, color):
    return sum(
        1 if s == c else 0
        for s, c in zip([int(e) for e in S], it.cycle([color, 1 - color]))
    )


def coloring(S, color):
    return len(
        [1 for s, c in zip([int(e) for e in S], it.cycle([color, 1 - color])) if s == c]
    )


def resolve():
    S = sys.stdin.readline().strip()
    print(min(coloring(S, 0), coloring(S, 1)))


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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
