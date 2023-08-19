import sys  # https://docs.python.org/ja/3/library/sys.html

MOD = 10**9 + 7


def sum_product_pairs_naive(N, A):
    s = 0
    for i in range(N - 1):
        for j in range(i + 1, N):
            s = (s + A[i] * A[j] % MOD) % MOD

    return s


def sum_product_pairs(N, A):
    B = A.copy()
    for i in range(N):
        B[i + 1] = (B[i] + B[i + 1]) % MOD

    s = 0
    for j in range(2, N + 1):
        s = (s + A[j] * B[j - 1] % MOD) % MOD

    return s


def resolve():
    N = int(sys.stdin.readline())
    A = [0] + [int(e) for e in sys.stdin.readline().split()]
    print(sum_product_pairs(N, A))


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
        input = """3
1 2 3"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
141421356 17320508 22360679 244949"""
        output = """437235829"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
