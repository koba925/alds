import sys
from io import StringIO
import unittest

def resolve():
    import re
    print("Yes" if re.match(r"^[A-Z][1-9][0-9]{5}[A-Z]$", input()) else "No")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """Q142857Z"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """AB912278C"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """X900000"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """K012345K"""
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
