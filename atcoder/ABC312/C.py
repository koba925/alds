from bisect import bisect_left, bisect_right

def resolve():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    A.sort()
    B.sort()

    left, right = 0, 10 ** 9 + 1
    while left < right:
        mid = (left + right) // 2
        a = bisect_right(A, mid)
        b = M - bisect_left(B, mid)
        if a >= b:
            right = mid
        else:
            left = mid + 1
    print(left)

# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 4
110 90 120
100 80 120 10000"""
        output = """110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
100000 100000 100000 100000 100000
100 200"""
        output = """201"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
100 100 100
80 120"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
