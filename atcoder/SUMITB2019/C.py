import sys


def resolve_mine():
    X = int(input())

    lower = upper = 0
    while lower <= X:
        lower += 100
        upper += 105
        if lower <= X <= upper:
            print("1")
            break
    else:
        print(0)


def resolve():
    X = int(input())
    memo = [True] + [False] * (X + 105)
    for i in range(0, X):
        if memo[i]:
            memo[i + 100] = True
            memo[i + 101] = True
            memo[i + 102] = True
            memo[i + 103] = True
            memo[i + 104] = True
            memo[i + 105] = True
    print(1 if memo[X] else 0)


# resolve()
# exit()

import unittest
from io import StringIO


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
        input = """615"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """217"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
