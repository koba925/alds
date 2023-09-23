import sys


def resolve_mine():
    Q, H, S, D = [int(e) for e in sys.stdin.readline().split()]
    N = int(sys.stdin.readline())
    bottles = [
        (Q * 100 // 25, Q, 25),
        (H * 100 // 50, H, 50),
        (S * 100 // 100, S, 100),
        (D * 100 // 200, D, 200),
    ]
    bottles.sort()
    if bottles[0][2] == 200:
        ans = N * 100 // bottles[0][2] * bottles[0][1]
        N = N * 100 % bottles[0][2] // 100
        ans += N * 100 // bottles[1][2] * bottles[1][1]
    else:
        ans = N * 100 // bottles[0][2] * bottles[0][1]

    print(ans)


def resolve():
    Q, H, S, D = [int(e) for e in sys.stdin.readline().split()]
    N = int(sys.stdin.readline())

    print((N // 2) * min(Q * 8, H * 4, S * 2, D) + (N % 2) * min(Q * 4, H * 2, S))


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
        input = """20 30 70 90
3"""
        output = """150"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10000 1000 100 10
1"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 100 1000 10000
1"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """12345678 87654321 12345678 87654321
123456789"""
        output = """1524157763907942"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
