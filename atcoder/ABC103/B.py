import sys


def rot(S, T):
    for i in range(len(S)):
        if S == T:
            return True
        S = S[-1] + S[:-1]
    return False


def resolve():
    S = sys.stdin.readline().strip()
    T = sys.stdin.readline().strip()
    print("Yes" if rot(S, T) else "No")


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
        input = """kyoto
tokyo"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abc
arc"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """aaaaaaaaaaaaaaab
aaaaaaaaaaaaaaab"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
