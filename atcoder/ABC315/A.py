import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    S = sys.stdin.readline().strip()
    print("".join([s for s in S if s not in "aeiou"]))


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
        input = """aaa"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """atcoder"""
        output = """tcdr"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """xyz"""
        output = """xyz"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """aaaabbbbcccc"""
        output = """bbbbcccc"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
