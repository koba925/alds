import sys
from io import StringIO
import unittest

def resolve():
    print(*reversed([input() for _ in range(int(input()))]), sep="\n")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3
Takahashi
Aoki
Snuke"""
        expected = """Snuke
Aoki
Takahashi"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """4
2023
Year
New
Happy"""
        expected = """Happy
New
Year
2023"""
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
