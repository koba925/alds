import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    PI = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    N = int(sys.stdin.readline())
    print(PI[: N + 2])


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
        input = """1"""
        output = """3.1"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """2"""
        output = """3.14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """32"""
        output = """3.14159265358979323846264338327950"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100"""
        output = """3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
