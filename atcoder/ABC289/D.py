def step_up(N, A, M, B, X):
    B = set(B)
    memo = [True] + [False] * X
    for i in range(1, X + 1):
        if i in B: continue
        for a in A:
            if i >= a and memo[i - a]:
                memo[i] = True
    return memo[X]

def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    M = int(input())
    B = [int(e) for e in input().split()]
    X = int(input())
    print("Yes" if step_up(N, A, M, B, X) else "No")

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
3 4 5
4
4 5 6 8
15"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2 3 4 5
4
3 4 5 6
8"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
2 5 7 8
5
2 9 10 11 19
20"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
