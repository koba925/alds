def resolve():
    MOD = 1000000007
    add_mod = lambda a, b: (a + b) % MOD

    N, M = [int(e) for e in input().split()]
    memo = [1] + [-1] * N
    for _ in range(M):
        a = int(input())
        memo[a] = 0

    for i in range(1, N + 1):
        if memo[i] == 0 : continue
        memo[i] = memo[i - 1]
        if i > 1: memo[i] = add_mod(memo[i], memo[i - 2])
    
    print(memo[N])

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
        input = """6 1
3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 2
4
5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 5
1
23
45
67
89"""
        output = """608200469"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
