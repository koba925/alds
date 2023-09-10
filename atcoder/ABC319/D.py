import sys


def resolve_mine():
    def minimum_width():
        def is_ok(W):
            if N == 1:
                return L[0] <= W
            lines = 1
            width = L[0]
            for i in range(1, len(L)):
                word = L[i]
                if width + 1 + word <= W:
                    width += 1 + word
                else:
                    width = word
                    lines += 1
                    if lines > M:
                        return False
            return True

        l, r = max(L), sum(L) + N
        while l < r:
            m = int((l + r) // 2)
            if is_ok(m):
                r = m
            else:
                l = m + 1
        return l

    N, M = [int(e) for e in sys.stdin.readline().split()]
    L = [int(e) for e in sys.stdin.readline().split()]
    print(minimum_width())


def resolve():
    def minimum_width():
        def is_ok(W):
            lines, width = 1, 0
            for l in L:
                if width + l <= W:
                    width += l
                else:
                    lines += 1
                    if lines > M:
                        return False
                    width = l
            return True

        left, right = max(L), sum(L)
        while left < right:
            mid = (left + right) // 2
            if is_ok(mid):
                right = mid
            else:
                left = mid + 1

        return left

    N, M = [int(e) for e in sys.stdin.readline().split()]
    L = [int(e) + 1 for e in sys.stdin.readline().split()]
    print(minimum_width() - 1)


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

    def test_1(self):
        input = """1 1
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_2(self):
        input = """1 2
1"""
        output = """1"""
        self.assertIO(input, output)

    def test_3(self):
        input = """3 3
2 2 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """13 3
9 5 2 7 1 8 8 2 1 5 2 3 6"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1
1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000"""
        output = """10000000009"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 8
8 55 26 97 48 37 47 35 55 5 17 62 2 60 23 99 73 34 75 7 46 82 84 29 41 32 31 52 32 60"""
        output = """189"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
