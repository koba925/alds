def resolve():
    N, S, K = [int(e) for e in input().split()]
    PQ = [[int(e) for e in input().split()] for _ in range(N)]
    price = sum(p * q for p, q in PQ)
    print(price if price >= S else price + K)

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
        input = """2 2000 500
1000 1
100 6"""
        output = """2100"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2000 500
1000 1
100 6
5000 1"""
        output = """6600"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2000 500
1000 1
1000 1"""
        output = """2000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
