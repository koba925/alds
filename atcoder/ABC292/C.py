# TK: 約数の個数（1～N）

import sys
from io import StringIO
import unittest

# def divisions(N):
#     i, result = 1, 0
#     while i * i <= N:
#         if N % i == 0:
#             result += 1
#             if N // i != i:
#                 result += 1
#         i += 1
#     return result

# def resolve():
#     N = int(input())
#     ans = 0
#     for i in range(1, N):
#         ans += divisions(i) * divisions(N - i)
#     print(ans)

def resolve():
    N = int(input())

    D = [0] * (N + 1)
    for a in range(1, N + 1):
        b = 1
        while a * b <= N:
            D[a * b] += 1
            b += 1

    ans = 0
    for i in range(1, N):
        ans += D[i] * D[N - i]
    print(ans)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4"""
        expected = """8"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """292"""
        expected = """10886"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """19876"""
        expected = """2219958"""
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
