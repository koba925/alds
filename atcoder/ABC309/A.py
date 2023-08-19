import sys

def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    diff = B - A
    print("Yes" if diff == 1 and A % 3 != 0 else "No") 

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
        input = """7 8"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 4"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
