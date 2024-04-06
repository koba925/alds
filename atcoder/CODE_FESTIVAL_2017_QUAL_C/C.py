import sys
from io import StringIO
import unittest

def resolve():
    s = input()

    count, left, right = 0, 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] == "x":
            left += 1
            count += 1
        elif s[right] == "x":
            right -= 1
            count += 1
        else:
            count = -1
            break
    print(count)


class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """xabxa"""
        expected = """2"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """ab"""
        expected = """-1"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """a"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """oxxx"""
        expected = """3"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
