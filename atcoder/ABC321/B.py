import sys


def resolve():
    N, X = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    A.sort()
    if sum(A[: len(A) - 1]) >= X:
        print(0)
    elif sum(A[1:]) < X:
        print(-1)
    else:
        print(X - sum(A[1 : len(A) - 1]))


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
        input = """5 180
40 60 80 50"""
        output = """70"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 100
100 100"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 200
0 0 99 99"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 480
59 98 88 54 70 24 8 94 46"""
        output = """45"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
