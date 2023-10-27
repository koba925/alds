def resolve():
    def distance(a, b, c, x):
        round = x // (a + c)
        rest = x - (a + c) * round
        return (a * b) * round + b * min(rest, a)
     
    A, B, C, D, E, F, X = [int(e) for e in input().split()]

    takahashi = distance(A, B, C, X)
    aoki = distance(D, E, F, X)

    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")

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
        input = """4 3 3 6 2 5 10"""
        output = """Takahashi"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 4 1 5 9 2"""
        output = """Aoki"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1 1 1 1 1 1"""
        output = """Draw"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
