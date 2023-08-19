import sys

from collections import deque

def farthest_bfs_noweight(start, adjs):             # longest distance / farthest node
# def shortest_bfs_noweight(start, goal, adjs):       # find shortest path / judge if connected
    def path(node):
        p = []
        while node != -1:
            p.append(node)
            node = parent[node]
        return reversed(p)

    def farthest_node():
        return (max(enumerate(distances), key=lambda x: x[1]))[0]
        
    l = len(adjs)
    q = deque()
    parent = [-1] * l
    distances = [-1] * l
    distances[start] = 0
    q.append(start)
    while q:
        node = q.popleft()
        # if node == goal:                            # find shortest path / judge if connected
            # return path(node)                       # find shortest path
            # return True                             # judge if connected
        for adj in adjs[node]:
            if distances[adj] == -1:
                distances[adj] = distances[node] + 1
                parent[adj] = node
                q.append(adj)
    # return []                                       # find shortest path
    # return False                                    # judge if connected
    return max(distances)                           # longest distance
    # return farthest_node()                          # farthest node

def add_one_edge(N1, N2, M, adjs):
    far1 = farthest_bfs_noweight(1, adjs)
    far2 = farthest_bfs_noweight(N1 + N2, adjs)
    return far1 + 1 + far2

def resolve():
    N1, N2, M = [int(e) for e in sys.stdin.readline().split()]
    adjs = [None] + [[] for _ in range(N1 + N2)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        adjs[a].append(b)
        adjs[b].append(a)
    print(add_one_edge(N1, N2, M, adjs))

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
