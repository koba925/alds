import collections as cl


def adjacent4(N, A):
    B = [4 if a % 4 == 0 else 2 if a % 2 == 0 else 1 for a in A]
    C = cl.Counter(B)
    if C[2] == 0:
        return C[1] <= C[4] + 1
    else:
        return C[1] <= C[4]


def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    print("Yes" if adjacent4(N, A) else "No")


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
1 10 100"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 4 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2
1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """6
2 7 1 8 2 8"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
