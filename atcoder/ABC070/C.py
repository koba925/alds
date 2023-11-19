def resolve_lib():
    import math
    print(math.lcm(*[int(input()) for _ in range(int(input()))]))

def resolve():
    import sys
    sys.setrecursionlimit(200000)
    import functools as ft

    gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
    mgcd = lambda A: ft.reduce(gcd, A)
    lcm = lambda a, b: a // gcd(a, b) * b
    mlcm = lambda A: ft.reduce(lcm, A)

    N = int(input())
    T = [int(input()) for _ in range(N)]
    print(mlcm(T))

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
        input = """2
2
3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
2
5
10
1000000000000000000
1000000000000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
