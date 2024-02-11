def resolve():
    import sys
    sys.setrecursionlimit(2000000)

    memo = {1: 0}

    def solve(n):
        if n in memo: return memo[n]
        if n % 2 == 0:
            ret = solve(n // 2) * 2 + n
        else:
            ret = solve(n // 2) + solve(n // 2 + 1) + n
        memo[n] = ret
        return ret

    print(solve(int(input())))

def resolve():

    import functools as ft

    @ft.cache
    def solve(n):
        if n == 1: return 0
        if n % 2 == 0: return solve(n // 2) * 2 + n
        return solve(n // 2) + solve(n // 2 + 1) + n

    print(solve(int(input())))

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
        input = """3"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """340"""
        output = """2888"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000000000000000"""
        output = """5655884811924144128"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
