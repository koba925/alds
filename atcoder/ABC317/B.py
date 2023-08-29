import sys


def resolve_by_loop():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    A.sort()
    for i in range(N - 1):
        if A[i] + 2 == A[i + 1]:
            print(A[i] + 1)


def resolve_by_sum():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]

    mina, maxa = min(A), max(A)
    total = (maxa + mina) * (maxa - mina + 1) // 2
    print(total - sum(A))


resolve_by_sum()
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
        input = """2
2 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3
2 3 5"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
3 1 4 5 9 2 6 8"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """16
152 153 154 147 148 149 158 159 160 155 156 157 144 145 146 150"""
        output = """151"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
