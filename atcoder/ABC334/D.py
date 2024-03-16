import sys
from io import StringIO
import unittest

def resolve():
    import itertools as it
    import bisect

    N, Q = [int(e) for e in input().split()]
    R = [int(e) for e in input().split()]

    S = list(it.accumulate(sorted(R), initial = 0))

    for _ in range(Q):
        x = int(input())
        i = bisect.bisect_left(S, x)
        if i > N:
            print(N)
        elif S[i] == x:
            print(i)
        else:
            print(i - 1)

class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """1 4
2
0
1
2
3"""
        output = """0
0
1
1"""
        self.assertIO(input, output)
    
    def test_sample1(self):
        input = """4 6
5 3 11 8
0
2
3
4
27
28"""
        expected = """0
0
1
1
4
4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """6 6
1 2 3 4 5 6
1
2
3
4
5
6"""
        expected = """1
1
2
2
2
3"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """2 2
1000000000 1000000000
200000000000000
1"""
        expected = """2
0"""
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
