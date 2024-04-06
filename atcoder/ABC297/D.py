import sys
from io import StringIO
import unittest

def resolve():
    A, B = [int(e) for e in input().split()]
    cnt = 0
    A, B = max(A, B), min(A, B)
    while B != 0:
        cnt += A // B
        A %= B
        A, B = B, A
    cnt -= 1
    print(cnt)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 8"""
        expected = """4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """1234567890 1234567890"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """1597 987"""
        expected = """15"""
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
