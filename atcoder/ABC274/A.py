import sys

def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    print(f"{B / A:.3f}")

# resolve()

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
        input = """7 4"""
        output = """0.571"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 3"""
        output = """0.429"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 1"""
        output = """0.500"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 10"""
        output = """1.000"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1 0"""
        output = """0.000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
