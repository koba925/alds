import sys
from io import StringIO
import unittest

def resolve():
    print(int((int(input()) + 10 - 1) // 10))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """27"""
        expected = """3"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """-13"""
        expected = """-1"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """40"""
        expected = """4"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """-20"""
        expected = """-2"""
        self.assertIO(input, expected)

    def test_sample5(self):
        input = """123456789123456789"""
        expected = """12345678912345679"""
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
