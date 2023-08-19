import sys

sys.setrecursionlimit(2000000)

def resolve():
    N = int(sys.stdin.readline())
    A = [list(s.strip()) for s in sys.stdin.readlines()]

    B = [row[:] for row in A]
    for i in range(N - 1):
        B[0][i + 1] = A[0][i]
        B[N - 1][i] = A[N - 1][i + 1]
        B[i][0] = A[i + 1][0]
        B[i + 1][N - 1] = A[i][N - 1]
    
    for row in B:
        print("".join(row))

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
0101
1101
1111
0000"""
        output = """1010
1101
0111
0001"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
11
11"""
        output = """11
11"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
01010
01001
10110
00110
01010"""
        output = """00101
11000
00111
00110
10100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
