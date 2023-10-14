import math

def resolve():
    N, X = [int(e) for e in input().split()]
    x = [int(e) for e in input().split()]
    print(math.gcd(*[xi - X for xi in x]))

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
        input = """3 3
1 7 11"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 81
33 105 57"""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 1
1000000000"""
        output = """999999999"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
