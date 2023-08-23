import sys

sys.setrecursionlimit(2000000)


def zero_one_TLE(N, A):
    def dfs(X, flip):
        if len(X) == 0:
            return True

        result = False
        if flip:
            if X[-1] == 1:
                result = dfs(X[:-1], flip)
            elif X[0] == 1:
                result = dfs(X[1:], not flip)
        else:
            if X[-1] == 0:
                result = dfs(X[:-1], flip)
            elif X[0] == 0:
                result = dfs(X[1:], not flip)
        return result

    return dfs(A, False)


from collections import deque


def zero_one_deque(N, A):
    X = deque(A)
    flip = 0

    while X:
        if X[0] == 1 - flip and X[-1] == 1 - flip:
            return False
        while X and X[-1] == flip:
            X.pop()
        if X and X[0] == flip:
            X.popleft()
            flip = 1 - flip

    return True


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print("Yes" if zero_one_TLE(N, A) else "No")
    # print("Yes" if zero_one_deque(N, A) else "No")


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
        input = """4
0 1 1 0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 0 0 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
0 0 0 1"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
