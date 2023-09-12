import sys
import functools as ft

sys.setrecursionlimit(2000000)


def max_matching_dfs_exhaustive(N, G):
    def dfs(used):
        if all(used):
            return 0

        v = used.index(False)
        used[v] = True
        ret = 0
        for w in range(v + 1, N):
            if not used[w]:
                used[w] = True
                ret = max(ret, G[v][w] + dfs(used))
                used[w] = False
        used[v] = False
        return ret

    used = [False] * N
    max_total = 0
    if N % 2 == 0:
        max_total = dfs(used)
    else:
        for v in range(N):
            used[v] = True
            max_total = max(max_total, dfs(used))
            used[v] = False

    return max_total


def max_matching_dp(N, G):
    dp = [0] * (1 << N)

    for b in range((1 << N) - 1):
        l = -1
        for i in range(N):
            if b >> i & 1 == 0:
                break
        for j in range(i, N):
            if b >> j & 1 == 0:
                nb = b | (1 << i) | (1 << j)
                dp[nb] = max(dp[nb], dp[b] + G[i][j])

    return dp[-1]


def resolve():
    N = int(sys.stdin.readline())
    G = [[0] * N for _ in range(N)]
    for i in range(N - 1):
        d = [int(e) for e in sys.stdin.readline().split()]
        for j in range(i + 1, N):
            G[i][j] = G[j][i] = d[j - i - 1]

    print(max_matching_dp(N, G))


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
        input = """2
        1"""
        output = """1"""
        self.assertIO(input, output)

    def test_2(self):
        input = """4
1 1 1
1 1
1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """4
1 5 4
7 8
6"""
        output = """13"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 2
3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """16
5 6 5 2 1 7 9 7 2 5 5 2 4 7 6
8 7 7 9 8 1 9 6 10 8 8 6 10 3
10 5 8 1 10 7 8 4 8 6 5 1 10
7 4 1 4 5 4 5 10 1 5 1 2
2 9 9 7 6 2 2 8 3 5 2
9 10 3 1 1 2 10 7 7 5
10 6 1 8 9 3 2 4 2
10 10 8 9 2 10 7 9
5 8 8 7 5 8 2
4 2 2 6 8 3
2 7 3 10 3
5 7 10 3
8 5 7
9 1
4"""
        output = """75"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
