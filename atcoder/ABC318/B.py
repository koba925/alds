import sys


def overlapping_sheets(N, A, B, C, D):
    S = [[False] * 100 for _ in range(100)]

    for i in range(N):
        for row in range(A[i], B[i]):
            for col in range(C[i], D[i]):
                S[row][col] = True

    return sum(sum(row) for row in S)


def resolve():
    N = int(sys.stdin.readline())
    A, B, C, D = zip(
        *[[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    )
    print(overlapping_sheets(N, A, B, C, D))


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
0 5 1 3
1 4 0 5
2 5 2 4"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
0 100 0 100
0 100 0 100"""
        output = """10000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
0 1 0 1
0 3 0 5
5 10 0 10"""
        output = """65"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
