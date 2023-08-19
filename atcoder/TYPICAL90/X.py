import sys

sys.setrecursionlimit(2000000)

def select_plus_minus_one(N, K, A, B):
    diff_total = sum(abs(a - b) for a, b in zip(A, B))
    return diff_total <= K and (K - diff_total) % 2 == 0

def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    B = [int(e) for e in sys.stdin.readline().split()]
    print("Yes" if select_plus_minus_one(N, K, A, B) else "No")

# resolve()

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
        input = """2 5
1 3
2 1"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
7 8 9
7 8 9"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 999999999
3 1 4 1 5 9 2
1 2 3 4 5 6 7"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
