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


import math
from functools import reduce


def gcd(*A):
    return reduce(math.gcd, A)


def lcm(*A):
    return reduce(lambda acc, e: acc * e // gcd(acc, e), A)



def semi_common_multiple(N, M, A):
    while A[0] % 2 == 0:
        for i in range(N):
            if A[i] % 2 != 0:
                return 0
            A[i] //= 2
        M //= 2

    for i in range(N):
        if A[i] % 2 == 0:
            return 0

    return (M // lcm(*A) + 1) // 2


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) // 2 for e in sys.stdin.readline().split()]
    print(semi_common_multiple(N, M, A))


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
        input = """2 50
6 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 100
14 22 40"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1000000000
6 6 2 6 2"""
        output = """166666667"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
