import sys

def minimum_coins_mine(N, A, B, C):
    min_coins = 10000
    a_upper = min(N // A, 9999)
    for a in range(0, a_upper + 1):
        a_rest = N - A * a
        b_upper = min(9999 - a, a_rest // B)
        for b in range(0, b_upper + 1):
            b_rest = a_rest - B * b
            c = b_rest // C
            if c < 0:
                break
            if b_rest % C == 0:
                min_coins = min(min_coins, a + b + c)
    return min_coins

def minimum_coins(N, A, B, C):
    min_coins = 10000
    for a in range(0, 10000):
        for b in range(0, 10000 - a):
            rest = N - A * a - B * b
            c = rest // C
            if c < 0:
                break
            if rest % C == 0:
                min_coins = min(min_coins, a + b + c)
    return min_coins

def resolve():
    N = int(sys.stdin.readline())
    A, B, C = [int(e) for e in sys.stdin.readline().split()]

    print(minimum_coins(N, A, B, C))

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
        input = """227
21 47 56"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999
1 5 10"""
        output = """1004"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """998244353
314159 265358 97932"""
        output = """3333"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """100000000
10001 10002 10003"""
        output = """9998"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
