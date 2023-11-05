# ABC327E - Maximize Rating
# TODO: understand 

def resolve():

    N = int(input())
    P = [int(e) for e in input().split()]

    C = 0.9
    memo = [0.0] * (N + 1)

    for i in range(N):
        memo[i + 1] = C * memo[i] + P[i]
        for j in reversed(range(0, i)):
            memo[j + 1] = max(C * memo[j] + P[i], memo[j + 1])

    w, ans = 0.0, -1200.0
    for k in range(1, N + 1):
        w = C * w + 1.0
        ans = max(ans, memo[k] / w - 1200.0 / k ** 0.5)
    
    print(ans)

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
1000 600 1200"""
        output = """256.735020470879931"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
600 1000 1200"""
        output = """261.423219407873376"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
100"""
        output = """-1100.000000000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
