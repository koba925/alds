import sys
import itertools as it


def cakecut(N, A):
    left = right = cut = 0
    total = sum(A)
    while left < N:
        while cut * 10 <= total:
            if cut * 10 == total:
                return True
            cut += A[right % N]
            right += 1
        cut -= A[left]
        left += 1
    return False


from bisect import bisect_left


def cakecut_editorial(N, A):
    total = sum(A)
    if total % 10 != 0:
        return False

    A += A
    B = [0] + list(it.accumulate(A))
    for left in range(N):
        target = total // 10 + B[left]
        right = bisect_left(B, target, left)
        if B[right] == target:
            return True
    return False


def resolve():
    N = int(sys.stdin.readline())
    A = [int(e) for e in sys.stdin.readline().split()]
    print("Yes" if cakecut_editorial(N, A) else "No")


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
        input = """1
10"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """10
1 1 1 1 1 1 1 1 1 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 18 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
1 9 1 9"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
