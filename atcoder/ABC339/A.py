def resolve():
    S = input()
    print(S[S.rfind(".")+1:])

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
        input = """atcoder.jp"""
        output = """jp"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """translate.google.com"""
        output = """com"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """.z"""
        output = """z"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """..........txt"""
        output = """txt"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
