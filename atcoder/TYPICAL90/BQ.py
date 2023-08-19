import sys

MOD = 10**9 + 7


def resolve_naive_TLE():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    ans = 1
    for i in range(N):
        ans *= max(K - i, K - 2)
        ans %= MOD
    print(ans)


def resolve_starstar_TLE():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    if N == 1:
        print(K)
    else:
        print(K * (K - 1) * (K - 2) ** (N - 2) % MOD)


def resolve_powmod():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    if N == 1:
        print(K)
    else:
        print(K * (K - 1) * pow(K - 2, N - 2, MOD) % MOD)


def power_mod_rec(n, p, m):
    def rec(p):
        if p == 0:
            return 1
        elif p % 2 == 0:
            return (rec(p // 2) ** 2) % m
        else:
            return (rec(p - 1) * n) % m

    return rec(p)

def power_mod(n, p, m):
    if p == 0: return 1
    if n == 0: return 0

    ans = 1
    while p > 0:
        if p & 1 == 1:
            ans = ans * n % m
        n = n * n % m
        p >>= 1
    return ans

def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    if N == 1:
        print(K)
    else:
        print(K * (K - 1) * power_mod(K - 2, N - 2, MOD) % MOD)


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

    def test_1(self):
        input = """1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_2(self):
        input = """1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_3(self):
        input = """2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """2 3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2021 617"""
        output = """53731843"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
