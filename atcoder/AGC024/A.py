import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    A, B, C, K = [int(e) for e in sys.stdin.readline().split()]

    print(A - B if K % 2 == 0 else B - A)


# resolve()
# exit()

import sys
import unittest
from io import StringIO


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
        input = """1 2 3 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 2 0"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000 1000000000 1000000000 1000000000000000000"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
