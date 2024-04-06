import sys
from io import StringIO
import unittest

def resolve():
    S, T = input(), input()
    for i, (s, t) in enumerate(zip(S + " ", T), 1):
        if s != t: break
    print(i)

class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """abc
abcc"""
        output = """4"""
        self.assertIO(input, output)
    
    
    def test_sample1(self):
        input = """atcoder
atcorder"""
        expected = """5"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """million
milllion"""
        expected = """5"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """vvwvw
vvvwvw"""
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
