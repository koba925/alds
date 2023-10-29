def resolve():
    import functools as ft

    MOD = 998244353

    inv_mod = lambda n: pow(n, MOD - 2, MOD)
    add_mod = lambda a, b: (a + b) % MOD
    mul_mod = lambda a, b: (a * b) % MOD

    N = int(input())
    A = [int(e) for e in input().split()]

    inv_n = inv_mod(N)
    p, expected = inv_n, 0
    for i in range(N):
        expected = add_mod(expected, mul_mod(A[i], p))
        p = add_mod(p, mul_mod(p, inv_n))

    print(expected)

def resolve():
    import functools as ft

    MOD = 998244353
    inv_mod = lambda n: pow(n, MOD - 2, MOD)
    add_mod = lambda a, b: (a + b) % MOD
    mul_mod = lambda a, b: (a * b) % MOD

    N = int(input())
    A = [0] + [int(e) for e in input().split()]

    inv_n = inv_mod(N)
    expected, sum_exp = [0] * (N + 1), 0
    for i in reversed(range(N + 1)):
        expected[i] = A[i] + mul_mod(inv_n, sum_exp)
        sum_exp = add_mod(sum_exp, expected[i])
    
    print(expected[0])

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
        input = """3
3 2 6"""
        output = """776412280"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
998244352"""
        output = """998244352"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
3 14 159 2653 58979 323846 2643383 27950288 419716939"""
        output = """545252774"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
