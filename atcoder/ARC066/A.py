import sys
from io import StringIO
import unittest

def resolve():
    def lining_up(N, A):
        A.sort()
        if N % 2 == 0:
            for i in range(N // 2):
                if not (A[2 * i] == A[2 * i + 1] == 2 * i + 1):
                    return 0
        else:
            if A[0] != 0:
                return 0
            for i in range(N // 2):
                if not (A[2 * i + 1] == A[2 * i + 2] == 2 * i + 2):
                    return 0
        return pow(2, N // 2, 10 ** 9 + 7)


    N = int(input())
    A = [int(e) for e in input().split()]
    print(lining_up(N, A))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
2 4 4 0 2"""
        expected = """4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """7
6 4 0 2 4 0 2"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """8
7 5 1 1 7 3 5 3"""
        expected = """16"""
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
