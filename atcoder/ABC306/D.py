import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    XY = [[int(e) for e in input().split()] for _ in range(N)]
    memo: list[tuple[int, int]] = [(0, 0)] * (N + 1)
    for i, [x, y] in enumerate(XY, 1):
        if x == 0: 
            memo[i] = (
                max(memo[i - 1][0],  memo[i - 1][0] + y, memo[i - 1][1] + y),
                memo[i - 1][1]
            )
        else:
            memo[i] = (
                memo[i - 1][0],
                max(memo[i - 1][0] + y, memo[i - 1][1])
            )
    print(max(memo[N]))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
1 100
1 300
0 -200
1 500
1 300"""
        expected = """600"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """4
0 -1
1 -2
0 -3
1 -4"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """15
1 900000000
0 600000000
1 -300000000
0 -700000000
1 200000000
1 300000000
0 -600000000
1 -900000000
1 600000000
1 -100000000
1 -400000000
0 900000000
0 200000000
1 -500000000
1 900000000"""
        expected = """4100000000"""
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
