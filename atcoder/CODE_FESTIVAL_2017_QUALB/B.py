import collections as cl

def problem_set(N, D, M, T):
    CD = cl.Counter(D)
    CT = cl.Counter(T)

    for t in CT:
        if CD[t] < CT[t]: return False
    return True

def resolve():
    N = int(input())
    D = [int(e) for e in input().split()]
    M = int(input())
    T = [int(e) for e in input().split()]

    print("YES" if problem_set(N, D, M, T) else "NO")

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
        input = """5
3 1 4 1 5
3
5 4 3"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
100 200 500 700 1200 1600 2000
6
100 200 500 700 1600 1600"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
800
5
100 100 100 100 100"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """15
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5
9
5 4 3 2 1 2 3 4 5"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
