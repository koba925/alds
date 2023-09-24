import sys

import itertools as it
import bisect


def resolve():
    N, M, P = [int(e) for e in sys.stdin.readline().split()]
    A = sorted([int(e) for e in sys.stdin.readline().split()])
    B = sorted([int(e) for e in sys.stdin.readline().split()])

    total = 0
    AA = list(it.accumulate(A, initial=0))
    for j in range(M):
        l = bisect.bisect(A, P - B[j])
        total += AA[l] + B[j] * l + P * (N - l)

    print(total)


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
        input = """2 2 7
3 5
6 1"""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 3 2
1
1 1 1"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 12 25514963
2436426 24979445 61648772 23690081 33933447 76190629 62703497
11047202 71407775 28894325 31963982 22804784 50968417 30302156 82631932 61735902 80895728 23078537 7723857"""
        output = """2115597124"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
