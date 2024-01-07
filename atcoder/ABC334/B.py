def resolve():
    A, M, L, R = [int(e) for e in input().split()]
    print((R - A) // M - (L - A + M - 1) // M + 1)

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
        input = """5 3 -1 6"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-2 2 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-177018739841739480 2436426 -80154573737296504 585335723211047198"""
        output = """273142010859"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
