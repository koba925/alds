import sys
from io import StringIO
import unittest

def resolve():
    N, K = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    S = K * (K + 1) // 2
    print(S - sum(a for a in set(A) if a <= K))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 5
1 6 3 1"""
        expected = """11"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """1 3
346"""
        expected = """6"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """10 158260522
877914575 24979445 623690081 262703497 24979445 1822804784 1430302156 1161735902 923078537 1189330739"""
        expected = """12523196466007058"""
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
