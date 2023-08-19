import sys

MOD = 10**9 + 7

# from functools import reduce
# def factorial(n):
#     return reduce(lambda acc, e: acc * e, range(1, n + 1))
#     ret = 1
#     while n > 1:
#         ret *= n
#         # ret %= MOD
#         n -= 1
#     return ret

# print(factorial(4))
# exit()


from math import factorial

def perm(n, r):
    return factorial(n) // factorial(r)


def comb(n, r):
    return factorial(n) // factorial(n - r) // factorial(r)


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


def factorization(N, M):
    ret = 1
    for f, p in prime_factorize(M):
        ret *= comb(p + N - 1, N - 1)
        ret %= MOD
    return ret


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    print(factorization(N, M))


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
        input = """2 6"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 12"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1000000000"""
        output = """957870001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
