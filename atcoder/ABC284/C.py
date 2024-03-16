import sys
from io import StringIO
import unittest

def resolve_uf():
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
    
    N, M = [int(e) for e in input().split()]
    groups = UnionFind(N)
    for _ in range(M):
        u, v = [int(e) for e in input().split()]
        u -= 1
        v -= 1
        groups.unite(u, v)
    print(groups.num_sets())

def resolve():
    import collections as cl

    N, M = [int(e) for e in input().split()]

    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = [int(e) for e in input().split()]
        u -= 1
        v -= 1
        G[u].append(v)
        G[v].append(u)

    groups = [-1] * N

    g = 0
    for s in range(N):
        if groups[s] != -1: continue

        togo = cl.deque()
        groups[s] = g
        togo.append(s)

        while togo:
            s = togo.pop()
            for t in G[s]:
                if groups[t] != -1: continue
                groups[t] = g
                togo.append(t)

        g += 1

    print(g)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5 3
1 2
1 3
4 5"""
        expected = """2"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5 0"""
        expected = """5"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """4 6
1 2
1 3
1 4
2 3
2 4
3 4"""
        expected = """1"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
