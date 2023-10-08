import functools as ft

MOD = 998244353
inv_mod = lambda n: pow(n, MOD - 2, MOD)
add_mod = lambda a, b: (a + b) % MOD
sub_mod = lambda a, b: (a - b) % MOD
mul_mod = lambda a, b: (a * b) % MOD
div_mod = lambda a, b: a * inv_mod(b) % MOD
sum_mod = lambda A: ft.reduce(add_mod, A)

def resolve():
    N, X = [int(e) for e in input().split()]
    T = [int(e) for e in input().split()]

    INV_N = inv_mod(N)
    div_N_mod = lambda a: a * INV_N % MOD

    memo = [1] + [0] * X
    for i in range(1, X + 1):
        for t in T:
            if t <= i:
                memo[i] = add_mod(memo[i], div_N_mod(memo[i - t]))

    print(div_N_mod(sum_mod(memo[-T[0] :])))

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
        input = """3 6
3 5 6"""
        output = """369720131"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 0
1 2 1 2 1"""
        output = """598946612"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 10000
1 2 3 4 5"""
        output = """586965467"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
