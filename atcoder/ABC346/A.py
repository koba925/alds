import sys
from io import StringIO
import unittest

def resolve():
    import itertools
    N, A = int(input()), [int(e) for e in input().split()]
    print(*[a1 * a2 for a1, a2 in itertools.pairwise(A)])

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
3 4 6"""
        expected = """12 24"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5
22 75 26 45 72"""
        expected = """1650 1950 1170 3240"""
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
