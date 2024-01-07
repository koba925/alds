def resolve():
    import itertools as it

    def double_factorial(N):
        if N % 2 == 1: return 0
        ans = 0
        N //= 2
        for p in it.count(1):
            n = 5 ** p
            if n > N: return ans
            ans += N // (5 ** p)

    N = int(input())
    print(double_factorial(N))

def resolve():
    def double_factorial(N):
        if N % 2 == 1: return 0
        ans = 0
        N //= 2
        while N > 0:
            N //= 5
            ans += N
        return ans
    
    N = int(input())
    print(double_factorial(N))

def resolve():
    def double_factorial(N):
        def _double_factorial(N):
            return 0 if N == 0 else N // 5 + _double_factorial(N // 5)

        return 0 if N % 2 == 1 else _double_factorial(N // 2)    

    N = int(input())
    print(double_factorial(N))

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

    def test_1(self):
        input = """50"""
        output = """6"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """12"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000000000"""
        output = """124999999999999995"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
