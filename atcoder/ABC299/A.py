def resolve():
    N = int(input())
    S = input()

    inside = False
    for s in S:
        if s == "|": inside = not inside
        if s == "*":
            print("in" if inside else "out")
            break

def resolve():
    N = int(input())
    S = input()

    print("in" if S.index("|") < S.index("*") < S.rindex("|") else "out")

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
        input = """10
.|..*...|."""
        output = """in"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
.|..|.*..."""
        output = """out"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
|*|"""
        output = """in"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
