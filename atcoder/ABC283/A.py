import sys
from io import StringIO
import unittest

def resolve():

    def pow_rec(A, B):
        if B == 0: return 1
        elif B % 2 == 0: return pow(A, B // 2) ** 2
        else: return pow(A, B - 1) * A

    def pow(A, B):
        ans = 1
        while B > 0:
            if B % 2 == 1:
                ans *= A
            A *= A
            B //= 2
        return ans

    A, B = [int(e) for e in input().split()]
    print(pow(A, B))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """4 3"""
        expected = """64"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5 5"""
        expected = """3125"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """8 1"""
        expected = """8"""
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
