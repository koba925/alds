def resolve():
    A, B = [int(e) for e in input().split()]
    print(A ** B + B ** A)

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
        input = """2 8"""
        output = """320"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 9"""
        output = """774840978"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 6"""
        output = """23401"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
