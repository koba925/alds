import sys

sys.setrecursionlimit(2000000)

from math import log

def base3(n):
    ans = []
    while n > 0:
        ans.append(n % 3)
        n //= 3
    return ans

def ternary_decompression(N, K):
    min_K = sum(base3(N))
    return min_K <= K and (min_K % 2 == K % 2)

def resolve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, K = [int(e) for e in sys.stdin.readline().split()]
        print("Yes" if ternary_decompression(N, K) else "No")

# resolve()

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
        input = """4
5 3
17 2
163 79
1000000000000000000 1000000000000000000"""
        output = """Yes
No
Yes
Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
