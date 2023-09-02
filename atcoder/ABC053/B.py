import sys


# def resolve():
#     s = sys.stdin.readline().strip()
#     print(len(s[s.find("A") : s.rfind("Z") + 1]))


def resolve():
    s = sys.stdin.readline().strip()

    for l, c in enumerate(s):
        if c == "A":
            break

    for r, c in reversed(list(enumerate(s))):
        if c == "Z":
            break

    print(r - l + 1)


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
        input = """QWERTYASDFZXCV"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ZABCZ"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """HASFJGHOGAKZZFEGA"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
