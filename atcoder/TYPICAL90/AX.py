import sys

MOD = 10 ** 9 + 7

def stair_jump(N, L):
    dp = [-1] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = (dp[i - 1] + (dp[i - L] if i >= L else 0)) % MOD
    return dp[N]

def resolve():
    N, L = [int(e) for e in sys.stdin.readline().split()]    
    print(stair_jump(N, L))

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
        input = """3 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6783 125"""
        output = """674508908"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
