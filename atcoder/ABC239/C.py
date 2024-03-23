import sys
from io import StringIO
import unittest

def resolve():
    import collections as cl
    S = input()
    L = len(S)
    C = cl.Counter(S)
    dup = sum(v * (v - 1) // 2 for k, v in C.items() if v > 1)
    if dup >= 1: dup -= 1
    print(L * (L - 1) // 2 - dup)


class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """abbb"""
        output = """4"""
        self.assertIO(input, output)
    
    def test_my_2(self):
        input = """aabb"""
        output = """5"""
        self.assertIO(input, output)
    
    def test_my_3(self):
        input = """aaabb"""
        output = """7"""
        self.assertIO(input, output)
    
    def test_my_4(self):
        input = """aaabbb"""
        output = """10"""
        self.assertIO(input, output)
    
    def test_my_5(self):
        input = """aa"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_my_6(self):
        input = """ab"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_sample1(self):
        input = """abc"""
        expected = """3"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """aaaaa"""
        expected = """1"""
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
