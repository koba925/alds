import sys

from itertools import permutations

MAX = 10001
def atcoder_ekiden(N, A, M, XY):
    def bad_order(order):
        return any(order[k + 1] in XY[order[k]] for k in range(N - 1))
    
    min_time = MAX
    for order in permutations(range(1, N + 1)):
        if bad_order(order):
            continue
        time = sum(A[order[k]][k + 1] for k in range(N))
        min_time = min(min_time, time)

    return -1 if min_time == MAX else min_time

def resolve():
    N = int(sys.stdin.readline())
    A = [None] + [[None] + [int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    M = int(sys.stdin.readline())
    XY = [None] + [[] for _ in range(N)]
    for _ in range(M):
        x, y = [int(e) for e in sys.stdin.readline().split()]
        XY[x].append(y)
        XY[y].append(x)
    print(atcoder_ekiden(N, A, M, XY))

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
        input = """3
1 10 100
10 1 100
100 10 1
1
1 2"""
        output = """111"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
3
1 2
1 3
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
1 10 100
10 1 100
100 10 1
0"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
