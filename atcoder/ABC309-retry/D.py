import sys

sys.setrecursionlimit(2000000)

from collections import deque

def farthest_bfs_noweight(start, adjs):             # longest distance
    l = len(adjs)
    q = deque()
    parent = [-1] * l
    distances = [-1] * l
    distances[start] = 0
    q.append(start)
    while q:
        node = q.popleft()
        for adj in adjs[node]:
            if distances[adj] == -1:
                distances[adj] = distances[node] + 1
                parent[adj] = node
                q.append(adj)
    return max(distances)                           # longest distance

def resolve():
    N1, N2, M = [int(e) for e in sys.stdin.readline().split()]
    adjs = [None] + [[] for _ in range(N1 + N2 + 1)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        adjs[a].append(b)
        adjs[b].append(a)
    
    far1 = farthest_bfs_noweight(1, adjs)
    far2 = farthest_bfs_noweight(N1 + N2, adjs)
    print(far1 + far2 + 1)

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
        input = """3 4 6
1 2
2 3
4 5
4 6
1 3
6 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 5 20
10 11
4 5
10 12
1 2
1 5
5 6
2 4
3 5
9 10
2 5
1 4
11 12
9 12
8 9
5 7
3 7
3 6
3 4
8 12
9 11"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
