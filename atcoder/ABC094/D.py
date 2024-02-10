def resolve():
    N = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    n = max(A)
    center = n // 2
    r = 0
    for a in A:
        if abs(center - a) < abs(center - r):
            r = a
    print(n, r)

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
        input = """5
6 9 4 2 11"""
        output = """11 6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
100 0"""
        output = """100 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
