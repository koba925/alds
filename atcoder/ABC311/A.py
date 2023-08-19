import sys

def first_abc_mine(N, S):
    a = b = c = False
    for i, char in enumerate(S, 1):
        if char == "A": a = True
        if char == "B": b = True
        if char == "C": c = True
        if a and b and c:
            return i

def first_abc_editorial(N, S):
    return max(S.find(s) + 1 for s in "ABC")

def resolve():
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    # print(first_abc_mine(N, S))
    print(first_abc_editorial(N, S))

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
        input = """5
ACABB"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
CABC"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
AABABBBABABBABABCABACAABCBACCA"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
