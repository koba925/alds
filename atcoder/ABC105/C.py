# TK: マイナス進法でも同じで行ける（ただしマイナスの割り算・余りの計算に注意）

import sys


def resolve():
    N = int(sys.stdin.readline())

    minus_mod = lambda a, b: a % -b
    minus_div = lambda a, b: -(a // -b)

    if N == 0:
        print("0")
    else:
        temp = []
        while N != 0:
            temp.append(str(minus_mod(N, -2)))
            N = minus_div(N, -2)

        print("".join(reversed(temp)))


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
        input = """-9"""
        output = """1011"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123456789"""
        output = """11000101011001101110100010101"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
