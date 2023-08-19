# LL: もう少し具体的に解けないか？

import sys

def approximate_equalization(N, A):
    p, q = divmod(sum(A), N)

    A.sort()
    B = [p] * (N - q) + [p + 1] * q

    return sum(abs(a - b) for a, b in zip (A, B)) // 2

def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print(approximate_equalization(N, A))


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

    def test_1(self):
        input = """4
1 1 1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_2(self):
        input = """4
1 2 1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_3(self):
        input = """4
0 0 0 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """4
4 7 3 7"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
313"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
999999997 999999999 4 3 2 4 999999990 8 999999991 999999993"""
        output = """2499999974"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
