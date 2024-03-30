import sys
from io import StringIO
import unittest

def resolve():
    def cost(i):
        c = i * A
        for j in range(N // 2):
            if S[i + j] != S[i + N - j - 1]:
                c += B
        return c

    N, A, B = [int(e) for e in input().split()]
    S = input()
    S = S + S
    print(min(cost(i) for i in range(N)))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5 1 2
rrefa"""
        expected = """3"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """8 1000000000 1000000000
bcdfcgaa"""
        expected = """4000000000"""
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
