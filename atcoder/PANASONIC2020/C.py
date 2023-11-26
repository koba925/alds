def resolve_WA():
    import math
    a, b, c = [int(e) for e in input().split()]
    print("Yes" if a ** 0.5 + b ** 0.5 < c ** 0.5 else "No")

def resolve():
    a, b, c = [int(e) for e in input().split()]
    print("Yes" if c > a + b and 4 * a * b < (c - a - b) ** 2 else "No")

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
        input = """2 3 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3 10"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
