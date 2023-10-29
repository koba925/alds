def resolve():
    from bisect import bisect_left, bisect_right

    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    A.sort()

    max_present = 0
    for i in range(N):
        j = bisect_left(A, A[i] + M)
        max_present = max(max_present, j - i)

    print(max_present)

def resolve():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    A.sort()
    A.append(2 * 10**9)

    right, max_presents = 0, 0
    for left in range(N):
        while A[right] < A[left] + M:
            right += 1
        max_presents = max(max_presents, right - left)
    
    print(max_presents)

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
        input = """8 6
2 3 5 7 11 13 17 19"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1
3 1 4 1 5 9 2 6 5 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 998244353
100000007 0 1755647 998244353 495 1000000000 1755648 503 1755649 998244853"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
