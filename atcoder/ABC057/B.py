import sys

sys.setrecursionlimit(2000000)

MAX = 10 ** 9

def manhattan(s, c):
    return abs(s[0] - c[0]) + abs(s[1] - c[1])

def find_nearest(s, M, C):
    min_dist = MAX
    min_j = -1
    for j in range(1, M + 1):
        dist = manhattan(s, C[j])
        if dist < min_dist:
            min_dist = dist
            min_j = j
    return min_j

def checkpoints(N, M, S, C):
    ans = []
    for i in range(1, N + 1):
        ans.append(find_nearest(S[i], M, C))
    return ans

def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    S = [None] + [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    C = [None] + [[int(e) for e in sys.stdin.readline().split()] for _ in range(M)]
    print(*checkpoints(N, M, S, C), sep="\n")

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
        input = """2 2
2 0
0 0
-1 0
1 0"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
10 10
-10 -10
3 3
1 2
2 3
3 5
3 5"""
        output = """3
1
2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
-100000000 -100000000
-100000000 100000000
100000000 -100000000
100000000 100000000
0 0
0 0
100000000 100000000
100000000 -100000000
-100000000 100000000
-100000000 -100000000"""
        output = """5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
