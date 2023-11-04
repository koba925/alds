def resolve():
    N, M = [int(e) for e in input().split()]

    from_one, to_n = set(), set()
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = [int(e) for e in input().split()]
        if a == 1: from_one.add(b)
        elif b == N: to_n.add(a)
    print("POSSIBLE" if from_one.intersection(to_n) else "IMPOSSIBLE")

def resolve():
    from heapq import heappush, heappop

    N, M = [int(e) for e in input().split()]

    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = [int(e) for e in input().split()]
        G[a].append(b)
        G[b].append(a)
    
    q, dist = [], [float("inf")] * (N + 1)
    heappush(q, 1)
    dist[1] = 0

    while q:
        here = heappop(q)
        for nxt in G[here]:
            if dist[nxt] > dist[here] + 1:
                dist[nxt] = dist[here] + 1
                heappush(q, nxt)

    print("POSSIBLE" if dist[N] <= 2 else "IMPOSSIBLE")

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
        input = """3 2
1 2
2 3"""
        output = """POSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3
1 2
2 3
3 4"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 99999"""
        output = """IMPOSSIBLE"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5 5
1 3
4 5
2 3
2 4
1 4"""
        output = """POSSIBLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
