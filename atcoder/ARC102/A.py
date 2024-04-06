import sys
from io import StringIO
import unittest

def resolve_TLE():
    N, K = [int(e) for e in input().split()]
    ans = 0
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if (a + b) % K != 0: continue
            for c in range(1, N + 1):
                if (b + c) % K != 0 or (c + a) % K != 0: continue
                ans += 1
    print(ans)

def resolve():
    pass

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 2"""
        expected = """9"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5 3"""
        expected = """1"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """31415 9265"""
        expected = """27"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """35897 932"""
        expected = """114191"""
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
