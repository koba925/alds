# TODO: 最大流問題として理解する

import sys


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    B = [int(e) for e in sys.stdin.readline().split()]
    slayed = 0
    for i in range(N):
        if A[i] >= B[i]:
            slayed += B[i]
        else:
            slayed += A[i]
            B[i] -= A[i]
            if A[i + 1] >= B[i]:
                slayed += B[i]
                A[i + 1] -= B[i]
            else:
                slayed += A[i + 1]
                A[i + 1] = 0
    print(slayed)


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
        input = """2
3 5 2
4 5"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
5 6 3 8
5 100 8"""
        output = """22"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
100 1 1
1 100"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
