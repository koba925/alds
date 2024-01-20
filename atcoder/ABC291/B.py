def resolve():
    N = int(input())
    X = [int(e) for e in input().split()]
    print(sum(sorted(X)[N:4*N]) / (3 * N))

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
        input = """1
10 100 20 50 30"""
        output = """33.333333333333336"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
3 3 3 4 5 6 7 8 99 100"""
        output = """5.500000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
