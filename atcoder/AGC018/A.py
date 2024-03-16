import sys
from io import StringIO
import unittest

def resolve():
    import math
    N, K = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    M, G = max(A), math.gcd(*A)

    print("POSSIBLE" if K <= M and (M - K) % G == 0 else "IMPOSSIBLE")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 7
9 3 4"""
        expected = """POSSIBLE"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 5
6 9 3"""
        expected = """IMPOSSIBLE"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """4 11
11 3 7 15"""
        expected = """POSSIBLE"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """5 12
10 2 8 6 4"""
        expected = """IMPOSSIBLE"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
