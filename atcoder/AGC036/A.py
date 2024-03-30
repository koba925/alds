import sys
from io import StringIO
import unittest

def resolve():
    S = int(input())
    x = (10 ** 9 - S % 10 ** 9) % 10 ** 9
    y = (S + x) // 10 ** 9
    print(f"0 0 1000000000 1 {x} {y}")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3"""
        expected = """1 0 2 2 0 1"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """100"""
        expected = """0 0 10 0 0 10"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """311114770564041497"""
        expected = """314159265 358979323 846264338 327950288 419716939 937510582"""
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
