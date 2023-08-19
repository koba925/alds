import sys

def string_transformation(S, T):
    trans = {}
    for s, t in zip(S, T):
        if s in trans and trans[s] != t:
            return False
        trans[s] = t
    return len(trans) == len(set(trans.values()))

def resolve():
    S = input()
    T = input()

    print("Yes" if string_transformation(S, T) else "No")

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
        input = """azzel
apple"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """chokudai
redcoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcdefghijklmnopqrstuvwxyz
ibyhqfrekavclxjstdwgpzmonu"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
