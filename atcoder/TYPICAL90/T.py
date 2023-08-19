import sys

from math import log2

def log_inequality_naive(a, b, c):
    return log2(a) < b * log2(c)

def log_inequality(a, b, c):
    return a < c ** b

def resolve():
    a, b, c = [int(e) for e in sys.stdin.readline().split()]
    # print("Yes" if log_inequality_naive(a, b, c) else "No")
    print("Yes" if log_inequality(a, b, c) else "No")

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
        input = """4 3 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """16 3 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 3 2"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
