import sys

sys.setrecursionlimit(2000000)

def souwa_1(N, K, A):
    return sum(A[i] * min(i + 1, K, N - K + 1, N - i) for i in range(N))

def souwa_2(N, K, A):
    for i in range(1, len(A)):
        A[i] += A[i - 1]
    A = [0] + A
    ans = 0
    for left in range(1, N - K + 2):
        right = left + K - 1
        ans += A[right] - A[left - 1]
    return ans

def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    # print(souwa_1(N, K, A))
    print(souwa_2(N, K, A))

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
        input = """5 3
1 2 4 8 16"""
        output = """49"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10
100000000 100000000 98667799 100000000 100000000 100000000 100000000 99986657 100000000 100000000 100000000 100000000 100000000 98995577 100000000 100000000 99999876 100000000 100000000 99999999"""
        output = """10988865195"""
        self.assertIO(input, output)

    def test_1(self):
        input = """4 4
1 2 3 4
"""

    def test_2(self):
        input = """5 4
1 2 3 4 5
"""
        output = """24"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
