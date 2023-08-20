import sys  # https://docs.python.org/ja/3/library/sys.html


def middle_day(M, D):
    for i in range(1, M + 1):
        D[i] += D[i - 1]

    last = D[M]
    mid = (last + 1) // 2

    for i in range(M + 1):
        if D[i] >= mid:
            return i, mid - D[i - 1]


def resolve():
    M = int(sys.stdin.readline())
    D = [0] + [int(e) for e in sys.stdin.readline().split()]
    print(*middle_day(M, D))


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
        input = """12
31 28 31 30 31 30 31 31 30 31 30 31"""
        output = """7 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
1"""
        output = """1 1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
3 1 4 1 5 9"""
        output = """5 3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
