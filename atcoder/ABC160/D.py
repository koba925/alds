def resolve():
    import collections as cl

    N, X, Y = [int(e) for e in input().split()]
    X -= 1
    Y -= 1
    
    memo = [[float("inf")] * N for _ in range(N)]
    for i in range(N): memo[i][i] = 0
    for i in range(N - 1):
        memo[i][i + 1] = memo[i + 1][i] = 1    
    memo[X][Y] = memo[Y][X] = 1

    for k in range(N):
        for i in range(N):
            for j in range(N):
                memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j])

    ans = cl.defaultdict(lambda: 0)   
    for i in range(N):
        for j in range(N):
            ans[memo[i][j]] += 1

    print(*[ans[n] // 2 for n in range(1, N)], sep="\n")

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
        input = """5 2 4"""
        output = """5
4
1
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1 3"""
        output = """3
0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 3 7"""
        output = """7
8
4
2
0
0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4 8"""
        output = """10
12
10
8
4
1
0
0
0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
