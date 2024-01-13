def resolve():
    import functools as ft

    MOD = 10 ** 9 + 7
    def mul_mod(a, b): return (a * b) % MOD
    def inv_mod(n): return pow(n, MOD - 2, MOD)
    def div_mod(a, b): return a * inv_mod(b) % MOD
    def dpow_mod(n, k): return ft.reduce(lambda acc, e: mul_mod(acc, e), range(n, n - k, - 1), 1)
    def fact_mod(n): return dpow_mod(n, n - 1)
    def comb_mod(n, k): return div_mod(dpow_mod(n, k), fact_mod(k))

    def knight(X, Y):
        if (X + Y) % 3 != 0 or X > 2 * Y or Y > 2 * X:
            return 0
        else:
            n = (2 * Y - X) // 3
            m = (2 * X - Y) // 3
            return comb_mod(n + m, n)

    X, Y = [int(e) for e in input().split()]
    print(knight(X, Y))

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

    def test_my_1(self):
        input = """7 5"""
        output = """4"""
        self.assertIO(input, output)
    
    def test_my_2(self):
        input = """25 35"""
        output = """15504"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """3 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999999 999999"""
        output = """151840682"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
