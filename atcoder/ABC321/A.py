import sys


def resolve():
    N = int(sys.stdin.readline())
    M = str(N)
    for i in range(len(M) - 1):
        if M[i] <= M[i + 1]:
            print("No")
            break
    else:
        print("Yes")


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
        input = """321"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """123"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """86411"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
