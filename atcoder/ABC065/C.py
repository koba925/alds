def resolve():
    import functools as ft

    MOD = 10 ** 9 + 7
    mul_mod = lambda a, b: (a * b) % MOD
    factorial_mod = lambda n: ft.reduce(lambda acc, e: mul_mod(acc, e), range(1, n + 1))

    N, M = [int(e) for e in input().split()]

    p = mul_mod(factorial_mod(N), factorial_mod(M))
    print(mul_mod(2, p) if N == M else p if abs(N - M) == 1 else 0)

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
        input = """2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 8"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000 100000"""
        output = """530123477"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
