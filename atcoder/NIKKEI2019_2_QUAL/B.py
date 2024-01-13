def resolve():
    import collections as cl

    MOD = 998244353
    mul_mod = lambda a, b: (a * b) % MOD
    # pow_mod = lambda a, b: pow(a, b, MOD)
    # pow_mod = lambda a, b: 1 if b == 0 else pow_mod(a, b // 2) ** 2 % MOD if b % 2 == 0 else mul_mod(pow(a, b - 1), a)

    def pow_mod(a, b):
        ret = 1
        a %= MOD
        while b > 0:
            if b % 2 == 1:
                ret = mul_mod(ret, a)
            a = mul_mod(a, a)
            b //= 2
        return ret

    def count_trees(N, D):
        DC = cl.Counter(D)
        if D[0] != 0 or DC[0] > 1: return 0

        ans = 1
        for d in range(1, N):
            ans = mul_mod(ans, pow_mod(DC[d - 1], DC[d]))
        return ans
    
    N = int(input())
    D = [int(e) for e in input().split()]
    print(count_trees(N, D))
    
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

    def test_a(self):
        input = """3
0 2 2"""
        output = """0"""
        self.assertIO(input, output)
    
    def test_b(self):
        input = """4
0 1 3 3"""
        output = """0"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """4
0 1 1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
0 3 2 1 2 2 1"""
        output = """24"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
