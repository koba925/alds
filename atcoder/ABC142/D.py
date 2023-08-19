import sys

def prime_factorize(N):
    prime_factors = []
    p = 2
    while p * p <= N:
        if N % p == 0:
            e = 0
            while N % p == 0:
                N //= p
                e += 1
            prime_factors.append((p, e))
        p += 1
    if N != 1:
        prime_factors.append((N, 1))
    return prime_factors

from math import gcd

def common_divisors(A, B):
    return len(prime_factorize(gcd(A, B))) + 1

def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]    
    print(common_divisors(A, B))

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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
