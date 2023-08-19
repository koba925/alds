import sys

from typing import NamedTuple, List, Optional
from heapq import heappush, heappop

INF = 2 ** 60

class Adjacent(NamedTuple):
    id: int
    dist: int = INF

class NextVert(NamedTuple):
    dist: int
    id: int

class Graph:
    def __init__(self, n: int, adjs: List[Adjacent]) -> None:
        self.n: int = n
        self.parents: List[Optional[int]] = [None] + [None] * n # 1-based
        self.dists: List[int] = [None] + [INF] * n # 1-based
        self.adjs: List[Adjacent] = adjs

    def shortest_path(self, start: int) -> None:
        next_verts: List[NextVert] = []
        self.dists[start] = 0
        heappush(next_verts, NextVert(0, start))

        while len(next_verts) > 0:
            dist, id = heappop(next_verts)
            if dist > self.dists[id]: continue
            for adj in self.adjs[id]:
                if self.dists[id] + adj.dist < self.dists[adj.id]:
                    self.dists[adj.id] = self.dists[id] + adj.dist
                    self.parents[adj.id] = id
                    heappush(next_verts, (self.dists[adj.id], adj.id))

    def path(self, goal: int) -> List[int]:
        p = [goal]
        vert = self.parents[goal]
        while vert is not None:
            p.append(vert)
            vert = self.parents[vert]
        return list(reversed(p))

# Shortest Path by Dijkstra (1-Based)
def resolve_dijkstra():
    N, M = [int(e) for e in sys.stdin.readline().split()]

    adjs = [None] + [[] for _ in range(N)] # 1-based
    for _ in range(M):
        a, b, t = [int(e) for e in sys.stdin.readline().split()]
        adjs[a].append(Adjacent(b, t))
        adjs[b].append(Adjacent(a, t))

    ans = INF
    for i in range(1, N + 1):
        g = Graph(N, adjs)
        g.shortest_path(i)
        path = g.path(1)
        far = max(g.dists[1:]) # 1-based
        ans = min(ans, far)
    print(ans)

# Shortest Path All Vertices by Floyd-Warshall (1-Based)
def resolve_floyd_warshall():
    INF = 10 ** 18
    N, M = [int(e) for e in sys.stdin.readline().split()]

    dp = [None] + [[None] + [INF] * N for _ in range(N)]
    for i in range(1, N + 1): dp[i][i] = 0
    for _ in range(M):
        a, b, t = [int(e) for e in sys.stdin.readline().split()]
        dp[a][b] = t
        dp[b][a] = t

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

    print(min(max(row[1:]) for row in dp[1:]))

def resolve():
    resolve_dijkstra()

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

    def test_入力例1(self):
        input = """3 2
1 2 10
2 3 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """5 5
1 2 12
2 3 14
3 4 7
4 5 9
5 1 18"""
        output = """26"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """4 6
1 2 1
2 3 1
3 4 1
4 1 1
1 3 1
4 2 1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
