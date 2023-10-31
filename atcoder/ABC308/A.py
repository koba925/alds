def resolve():
    import itertools as it
        
    S = [int(e) for e in input().split()]

    increasing = lambda: all(a <= b for a, b in it.pairwise(S))
    in_range = lambda lower, upper: all(lower <= s <= upper for s in S)
    multiple = lambda base: all(s % base == 0 for s in S)

    print("Yes" if increasing() and in_range(100, 675) and multiple(25) else "No")

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
        input = """125 175 250 300 400 525 600 650"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 250 300 400 325 575 625 675"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 23 24 145 301 413 631 632"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
