def longest_palindrome(S):
    L = len(S)
    for l in reversed(range(1, L + 1)):
        for i in range(0, L - l + 1):
            if S[i:i + l] == S[i:i + l][::-1]:
                return l

def resolve():
    print(longest_palindrome(input()))

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
        input = """TOYOTA"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ABCDEFG"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """AAAAAAAAAA"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
