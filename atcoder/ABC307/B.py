def is_palindrome(s):
    return s == s[::-1]

def racecar(N, S):
    for a in S:
        for b in S:
            if a == b: continue
            if is_palindrome(a + b):
                return True
    return False

def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    print("Yes" if racecar(N, S) else "No")

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
ab
ccef
da
a
fe"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
a
b
aba"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
