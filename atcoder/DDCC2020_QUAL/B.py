def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    total2 = sum(A) * 2
    mid2 = total2 // 2
    sum_len2 = 0
    for i in range(N):
        sum_len2 += A[i] * 2
        if sum_len2 >= mid2:
            break
    left = mid2 - (sum_len2 - A[i] * 2)
    right = sum_len2 - mid2
    ans = min(left, right)
    print(ans)


import itertools as it


def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    AA = list(it.accumulate(A, initial=0))

    ans = float("inf")
    for i in range(N + 1):
        left = AA[i]
        right = AA[N] - AA[i]
        ans = min(ans, abs(left - right))

    print(ans)


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
        input = """3
2 4 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """12
100 104 102 105 103 103 101 105 104 102 104 101"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
