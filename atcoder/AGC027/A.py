import sys


def candy_distribution(N, X, A):
    A.sort()
    for i in range(N):
        X -= A[i]
        if X <= 0:
            break
    return i + 1 if X == 0 else i


def resolve():
    N, X = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    print(candy_distribution(N, X, A))


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
        input = """3 70
20 30 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 10
20 30 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1111
1 10 100 1000"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 10
20 20"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
