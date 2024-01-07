def resolve():
    MOD = 10 ** 9 + 7
    inv_mod = lambda n: pow(n, MOD - 2, MOD)
    add_mod = lambda a, b: (a + b) % MOD
    mul_mod = lambda a, b: (a * b) % MOD

    N, K = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    inv_2 = inv_mod(2)

    inv_cnt = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] > A[j]: 
                inv_cnt = add_mod(inv_cnt, mul_mod(mul_mod(K,  K + 1), inv_2))
            elif A[i] < A[j]: 
                inv_cnt = add_mod(inv_cnt, mul_mod(mul_mod(K - 1,  K), inv_2))
    
    print(inv_cnt)
    
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
        input = """2 2
2 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5
1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 998244353
10 9 8 7 5 6 3 4 2 1"""
        output = """185297239"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
