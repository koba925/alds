import sys


def resolve():
    N = int(sys.stdin.readline())
    p = 1
    for i in range(1, N + 1):
        p = (p * i) % (10**9 + 7)
    print(p)


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
        input = """3"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10"""
        output = """3628800"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000"""
        output = """457992974"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
