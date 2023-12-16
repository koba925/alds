def resolve():
    N, M = [int(e) for e in input().split()]
    XY = [[int(e) - 1 for e in input().split()] for _ in range(M)]

    B = [1] * N
    R = [True] + [False] * (N - 1)

    for x, y in XY:
        B[x] -= 1
        R[y] = R[y] or R[x]
        if B[x] == 0: R[x] = False
        B[y] += 1

    print(sum(b > 0 and r for b, r in zip(B, R)))


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

    def test_入力例1(self):
        input = """3 2
1 2
2 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 3
1 2
2 3
2 3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 4
1 2
2 3
4 1
3 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
