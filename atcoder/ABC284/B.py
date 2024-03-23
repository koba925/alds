import sys
from io import StringIO
import unittest

def resolve():
    T = int(input())
    for _ in range(T):
        N, A = int(input()), [int(e) for e in input().split()]
        print(len([a for a in A if a % 2 != 0]))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4
3
1 2 3
2
20 23
10
6 10 4 1 5 9 8 6 5 1
1
1000000000"""
        expected = """2
1
5
0"""
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
