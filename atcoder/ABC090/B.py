import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    print(len([n for n in range(A, B + 1) if str(n) == str(n)[::-1]]))


# resolve()
# exit()


import sys
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
        input = """11009 11332"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """31415 92653"""
        output = """612"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
