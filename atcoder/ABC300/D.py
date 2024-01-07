import sys

def primes_below(limit):
    primes, is_prime = [], [True] * limit
    for n in range(2, limit):
        if not is_prime[n]: continue
        primes.append(n)
        for m in range(2 * n, limit, n):
            is_prime[m] = False
    return primes

def aabcc(N):
    prime_limit = 1000000
    primes = primes_below(prime_limit)
    nprime = len(primes)

    ans = 0
    for ia in range(0, nprime - 2):
        a = primes[ia]
        for ib in range(ia + 1, nprime - 1):
            b = primes[ib]
            aab = a ** 2 * b
            if aab * primes[ib + 1] ** 2 > N:
                break
            for ic in range(ib + 1, nprime):
                c = primes[ic]
                if aab * c ** 2 <= N:
                    ans += 1
                else:
                    break
    return ans

def resolve():
    N = int(sys.stdin.readline())
    print(aabcc(N))

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
        input = """1000"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000000"""
        output = """2817785"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
