def resolve():
    N, M = [int(e) for e in input().split()]
    S = input()
    T = input()
    if T.startswith(S) and T.endswith(S):
        print(0)
    elif T.startswith(S):
        print(1)
    elif T.endswith(S):
        print(2)
    else:
        print(3)


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
        input = """3 7
abc
abcdefg"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
abc
aabc"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3
abc
xyz"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3 3
aaa
aaa"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
