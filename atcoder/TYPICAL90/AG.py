import sys

def divceil(a, x): return int(-(-a // x))

def not_too_bright(H, W):
    if H == 1 or W == 1:
        return H * W
    else:
        return divceil(H, 2) * divceil(W, 2)

def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    print(not_too_bright(H, W))

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
        input = """2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 6"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
