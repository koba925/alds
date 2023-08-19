import sys  # https://docs.python.org/ja/3/library/sys.html


def tancho(N, A):
    left, right, count = 0, 0, 0

    while left < N:
        while right < N - 1 and A[right] < A[right + 1]:
            right += 1
        l = right - left + 1
        # count += l * (l + 1) // 2
        # left = right = right + 1
        count += l
        left += 1
        right = max(right, left)

    return count


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print(tancho(N, A))


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
        input = """5
1 2 3 2 1"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """4
1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6
3 3 4 1 2 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """6
1 5 2 3 4 2"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
