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

def sum_divisors_prime_factorize(N):
    primes = prime_factorize(N)
    sum_div = 1
    for n, p in primes:
        sum_div *= (n ** (p + 1) - 1) // (n - 1)
    return sum_div

def sum_divisors_loop(N):
    i, divisors = 1, []
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if N // i != i:
                divisors.append(N // i)
        i += 1
    return sum(divisors)

def kanzensu(N):
    sum_div = sum_divisors_loop(N)
    return ("Deficient" if sum_div < 2 * N else
            "Abundant" if 2 * N < sum_div else
            "Perfect")

def resolve():
    N = int(sys.stdin.readline())    
    print(kanzensu(N))

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

    def test_入力例1(self):
        input = """6"""
        output = """Perfect"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """24"""
        output = """Abundant"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """27"""
        output = """Deficient"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """945"""
        output = """Abundant"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
