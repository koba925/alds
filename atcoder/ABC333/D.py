def resolve():
    import sys
    sys.setrecursionlimit(2000000)

    N = int(input())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    visited = [True] + [False] * (N - 1)

    def node_num(s):
        visited[s] = True
        num = 0
        for t in G[s]:
            if not visited[t]:
                num += node_num(t)
        return num + 1

    node_nums = []
    for s in G[0]:
        node_nums.append(node_num(s))
    print(sum(sorted(node_nums)[:-1]) + 1)
    
def resolve():
    class UnionFind:
    
        def __init__(self, size):
            self.size = size
            self._parent = list(range(size))
            self._elems = [1] * size
    
        def _ancestor(self, x):
            while self._parent[x] != x:
                x = self._parent[x]
            return x
    
        def unite(self, x, y):
            x = self._ancestor(x)
            y = self._ancestor(y)
    
            if x == y:
                return
    
            # union by size
            if self._elems[x] < self._elems[y]:
                x, y = y, x
            self._parent[y] = x
            self._elems[x] += self._elems[y]
    
        def same(self, x, y):    
            return self._ancestor(x) == self._ancestor(y)
        
        def num_sets(self):
            return len([1 for i in range(self.size) if self._parent[i] == i])
        
        def sizes(self):
            return [self._elems[i] for i in range(self.size) if self._parent[i] == i]
    
    N = int(input())
    groups = UnionFind(N)
    for _ in range(N - 1):
        u, v = [int(e) for e in input().split()]
        if u != 1 and v != 1:
            groups.unite(u - 1, v - 1)
    print(sum(sorted(groups.sizes()[1:])[:-1]) + 1)

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
        input = """9
1 2
2 3
2 4
2 5
1 6
6 7
7 8
7 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
1 2
2 3
2 4
3 5
3 6"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """24
3 6
7 17
7 20
7 11
14 18
17 21
6 19
5 22
9 24
11 14
6 23
8 17
9 12
4 17
2 15
1 17
3 9
10 16
7 13
2 16
1 16
5 7
1 3"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
