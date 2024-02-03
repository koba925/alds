def resolve():
    N, M = [int(e) for e in input().split()]
    A = [] if M == 0 else [int(e) for e in input().split()]

    ans, i, left, right = [], 0, 1, 1
    while i < M:
        while i < M and right == A[i]:
            right += 1
            i += 1
        ans += reversed(range(left,right + 1))
        left = right = right + 1
    ans += range(right, N + 1)
    print(*ans)

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
        input = """5 3
1 3 4"""
        output = """2 1 5 4 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 0"""
        output = """1 2 3 4 5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 6
1 2 3 7 8 9"""
        output = """4 3 2 1 5 6 10 9 8 7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
