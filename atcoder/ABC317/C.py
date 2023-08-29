import sys

sys.setrecursionlimit(2000000)


def days(N, G):
    def dfs(s):
        def _dfs(n, dist):
            nonlocal max_dist

            max_dist = max(max_dist, dist)
            visited[n] = True
            for nn, nc in G[n]:
                if not visited[nn]:
                    _dfs(nn, dist + nc)
            visited[n] = False

        max_dist = 0
        visited = [None] + [False] * N
        _dfs(s, 0)
        return max_dist

    return max(dfs(s) for s in range(1, N + 1))


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    G = [None] + [[] for _ in range(N)]
    for _ in range(M):
        a, b, c = [int(e) for e in sys.stdin.readline().split()]
        G[a].append((b, c))
        G[b].append((a, c))

    print(days(N, G))


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
        input = """4 4
1 2 1
2 3 10
1 3 100
1 4 1000"""
        output = """1110"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 1
5 9 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 13
1 2 1
1 10 1
2 3 1
3 4 4
4 7 2
4 8 1
5 8 1
5 9 3
6 8 1
6 9 5
7 8 1
7 9 4
9 10 3"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
