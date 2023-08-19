import sys

from collections import deque

def resolve_deque():
    N, Q = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    # A = deque(A)
    for _ in range(Q):
        T, x, y = [int(e) for e in sys.stdin.readline().split()]
        x, y = x - 1, y - 1
        if T == 1:
            A[x], A[y] = A[y], A[x]
        elif T == 2:
            A.appendleft(A.pop())
        elif T == 3:
            print(A[x])

def resolve_shift():
    def pos(p):
        return (p - 1 - shift) % N

    N, Q = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]

    shift = 0
    for _ in range(Q):
        T, x, y = [int(e) for e in sys.stdin.readline().split()]
        if T == 1:
            A[pos(x)], A[pos(y)] = A[pos(y)], A[pos(x)]
        elif T == 2:
            shift += 1
        elif T == 3:
            print(A[pos(x)])

def resolve():
    # resolve_deque()
    resolve_shift()

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
        input = """8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 6
16 7 10 2 9 18 15 20 5
2 0 0
1 1 4
2 0 0
1 8 5
2 0 0
3 6 0"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """11 18
23 92 85 34 21 63 12 9 81 44 96
3 10 0
3 5 0
1 3 4
2 0 0
1 4 11
3 11 0
1 3 5
2 0 0
2 0 0
3 9 0
2 0 0
3 6 0
3 10 0
1 6 11
2 0 0
3 10 0
3 4 0
3 5 0"""
        output = """44
21
34
63
85
63
21
34
96"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
