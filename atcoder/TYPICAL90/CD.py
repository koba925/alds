# LL: 割った余りの四則演算は割り算に注意（逆元を使う） https://qiita.com/_oga_/items/177c4e8bae46211a4339

import sys  # https://docs.python.org/ja/3/library/sys.html

MOD = 10**9 + 7


def num_digits(n):
    return len(str(n))


def inverse(x, mod):
    return pow(x % mod, mod - 2, mod)


def sum_between(l, r):
    return (r + l) * (r - l + 1) % MOD * inverse(2, MOD)


def counting_numbers(L, R):
    letters = 0
    digits = num_digits(L)
    rdigits = num_digits(R)
    while digits <= rdigits:
        l = max(L, 10 ** (digits - 1))
        r = min(R, 10**digits - 1)
        letters = (letters + sum_between(l, r) * digits % MOD) % MOD
        digits += 1
    return letters


def resolve():
    L, R = [int(e) for e in sys.stdin.readline().split()]
    print(counting_numbers(L, R))


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
        input = """3 5"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """98 100"""
        output = """694"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1001 869120"""
        output = """59367733"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """381453331666495446 746254773042091083"""
        output = """584127830"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
