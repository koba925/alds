import sys
from io import StringIO
import unittest

def resolve():
    N, X = [int(e) for e in input().split()]
    AB = [[int(e) for e in input().split()] for _ in range(N)]
    memo = [[False] * (X + 1) for _ in range(5001)]
    memo[0][0] = True
    j = 1
    for a, b in AB:
        for i in range(b):
            for x in range(X + 1):
                memo[j][x] = memo[j - 1][x]
                if x >= a:
                    memo[j][x] = memo[j][x]  or memo[j - 1][x - a]
            j += 1
    print("Yes" if any(memo[i][X] for i in range(j)) else "No")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 19
2 3
5 6"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """2 18
2 3
5 6"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """3 1001
1 1
2 1
100 10"""
        expected = """Yes"""
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
