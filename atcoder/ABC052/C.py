import sys

sys.setrecursionlimit(2000000)


def prime_factorize(N):
    factors = []
    n = 2
    while n * n <= N:
        if N % n == 0:
            p = 0
            while N % n == 0:
                N //= n
                p += 1
            factors.append((n, p))
        n += 1
    if N != 1:
        factors.append((N, 1))
    return factors


from collections import defaultdict

MOD = 10 ** 9 + 7

def factors_of_factorial(N):
    pfs = defaultdict(int)
    for i in range(2, N + 1):
        for n, p in prime_factorize(i):
            pfs[n] += p
    ret = 1
    for _, p in pfs.items():
        ret = ret * (p + 1) % MOD
    return ret


def resolve():
    N = int(sys.stdin.readline())
    print(factors_of_factorial(N))


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
        input = """3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000"""
        output = """972926972"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
