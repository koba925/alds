def resolve():
    def divceil(a, x): return int((a + x - 1) // x)

    N, S, M, L = [int(e) for e in input().split()]

    min_price = float("inf")
    for s in range(divceil(N, 6) + 1):
        for m in range(divceil(N, 8) + 1):
            for l in range(divceil(N, 12) + 1):
                if 6 * s + 8 * m + 12 * l >= N:
                    price = s * S + m * M + l * L
                    min_price = min(min_price, price)
    print(min_price)

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
        input = """16 120 150 200"""
        output = """300"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 100 50 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99 600 800 1200"""
        output = """10000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
