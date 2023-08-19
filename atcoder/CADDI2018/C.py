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

def product_and_gcd(N, P):
    gcd = 1
    for f, p in prime_factorize(P):
        gcd *= (f ** (p // N))
    return gcd

def resolve():
    N, P = [int(e) for e in sys.stdin.readline().split()]    
    print(product_and_gcd(N, P))

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
        input = """3 24"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 111"""
        output = """111"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4 972439611840"""
        output = """206"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
