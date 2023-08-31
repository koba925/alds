import sys


def exponential(X):
    if X <= 3:
        return 1
    max_exp = 0
    base = 2
    while base**2 <= X:
        power = 2
        while base**power <= X:
            max_exp = max(max_exp, base**power)
            power += 1
        base += 1
    return max_exp


def resolve():
    X = int(sys.stdin.readline())
    print(exponential(X))


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
        input = """10"""
        output = """9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """999"""
        output = """961"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
