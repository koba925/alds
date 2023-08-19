import sys  # https://docs.python.org/ja/3/library/sys.html


def two_by_two(H, W, A, B):
    def incdec(M, row, col, delta):
        M[row][col] += delta
        M[row + 1][col] += delta
        M[row][col + 1] += delta
        M[row + 1][col + 1] += delta

    times = 0
    for row in range(H - 1):
        for col in range(W - 1):
            delta = B[row][col] - A[row][col]
            times += abs(delta)
            incdec(A, row, col, delta)
        if A[row][W - 1] != B[row][W - 1]:
            return False, 0
    for col in range(W):
        if A[row][col] != B[row][col]:
            return False, 0

    return True, times

def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    A = [[int(e) for e in sys.stdin.readline().split()] for _ in range(H)]
    B = [[int(e) for e in sys.stdin.readline().split()] for _ in range(H)]
    possible, times = two_by_two(H, W, A, B)
    print(f"Yes\n{times}" if possible else "No")


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
        input = """3 3
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0"""
        output = """Yes
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 1 0
0 0 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
6 17 18 29 22
39 50 25 39 25
34 34 8 25 17
28 48 25 47 42
27 47 24 32 28
4 6 3 29 28
48 50 21 48 29
44 44 19 47 28
4 49 46 29 28
4 49 45 1 1"""
        output = """Yes
140"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
