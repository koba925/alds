import sys
from io import StringIO
import unittest

def resolve():
    from itertools import accumulate
    from bisect import bisect

    N, T = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    B = list(accumulate(A, initial=0))
    T %= B[-1]
    m = bisect(B, T)
    s = T - B[m - 1]
    print(m, s)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 600
180 240 120"""
        expected = """1 60"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 281
94 94 94"""
        expected = """3 93"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """10 5678912340
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        expected = """6 678912340"""
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
