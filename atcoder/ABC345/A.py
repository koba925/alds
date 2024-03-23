import sys
from io import StringIO
import unittest

def resolve():
    import re
    print("Yes" if re.match(r"^<=+>$", input())  else "No")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """<====>"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """==>"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """<>>"""
        expected = """No"""
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
