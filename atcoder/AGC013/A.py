import itertools as it


def sign(n):
    return 1 if n > 0 else -1 if n < 0 else 0


def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    ans, prev_delta = 1, 0
    for prev_a, a in it.pairwise(A):
        delta = sign(a - prev_a)
        if prev_delta == 0:
            prev_delta = delta
        elif delta != 0 and delta != prev_delta:
            prev_delta = 0
            ans += 1

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
        input = """6
1 2 3 2 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
1 2 1 2 1 2 1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
1 2 3 2 1 999999999 1000000000"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
