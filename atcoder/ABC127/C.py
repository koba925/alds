import sys

def resolve_for():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    L, R = [], []
    for _ in range(M):
        l, r = [int(e) for e in sys.stdin.readline().split()]
        L.append(l)
        R.append(r)
    print(max(0, min(R) - max(L) + 1))

def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    LR = [[int(e) for e in sys.stdin.readline().split()] for _ in range(M)]
    leftmost, rightmost = max([lr[0] for lr in LR]), min([lr[1] for lr in LR])
    print(max(0, rightmost - leftmost + 1))

def resolve_zip():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    L, R = zip(*[[int(e) for e in sys.stdin.readline().split()] for _ in range(M)])
    print(max(0, min(R) - max(L) + 1))

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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
