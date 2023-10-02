import sys


def resolve():
    N, A, B = [int(e) for e in sys.stdin.readline().split()]
    print((B - A) * (N - 2) + 1 if (N > 1 and A <= B) or (N == 1 and A == B) else 0)


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
        input = """4 4 6"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4 3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 7 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 3 3"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
