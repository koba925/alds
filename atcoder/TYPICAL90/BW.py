import sys


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


from math import log2, ceil


def magic_for_balls(N):
    factors = prime_factorize(N)
    nfactor = sum([factor[1] for factor in factors])
    return 0 if nfactor == 1 else int(ceil(log2(nfactor)))


def resolve():
    N = int(sys.stdin.readline())
    print(magic_for_balls(N))


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
        input = """42"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """48"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """54"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """53"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
