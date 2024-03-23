import sys
from io import StringIO
import unittest

def resolve():
    print(int(input()) // 10)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """47"""
        expected = """4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """-24"""
        expected = """-3"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """50"""
        expected = """5"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """-30"""
        expected = """-3"""
        self.assertIO(input, expected)

    def test_sample5(self):
        input = """987654321987654321"""
        expected = """98765432198765432"""
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
