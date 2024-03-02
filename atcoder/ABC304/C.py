def resolve():
    import collections as cl

    def solve(N, D, X, Y):
        G = [[] for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= D ** 2:
                    G[i].append(j)
                    G[j].append(i)
        
        infected = [False] * N
        infected[0] = True
        q = [0]
        while q:
            p = q.pop()
            for a in G[p]:
                if not infected[a]:
                    infected[a] = True
                    q.append(a)

        return infected
    
    N, D = [int(e) for e in input().split()]
    X, Y = zip(*[[int(e) for e in input().split()] for _ in range(N)])
    print(*["Yes" if infected else "No" for infected in solve(N, D, X, Y)], sep="\n")

def resolve_unionfind():
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

    def solve(N, D, X, Y):
        return G 
    
    N, D = [int(e) for e in input().split()]
    X, Y = zip(*[[int(e) for e in input().split()] for _ in range(N)])

    G = UnionFind(N)
    for i in range(N):
        for j in range(i + 1, N):
            if (X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2 <= D ** 2:
                G.unite(i, j)

    print(*["Yes" if G.same(0, n) else "No" for n in range(N)], sep="\n")

def resolve_nograph():
    import collections as cl

    def solve(N, D, XY):
        infected = [False] * N
        q = cl.deque([0])
        infected[0] = True
        while q:
            p = q.pop()
            x1, y1 = XY[p]
            for i in range(N):
                if infected[i]: continue
                x2, y2 = XY[i]
                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= D ** 2:
                    infected[i] = True
                    q.append(i)

        return infected
    
    N, D = [int(e) for e in input().split()]
    XY = [[int(e) for e in input().split()] for _ in range(N)]
    print(*["Yes" if infected else "No" for infected in solve(N, D, XY)], sep="\n")

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
        input = """4 5
2 -1
3 1
8 8
0 5"""
        output = """Yes
Yes
No
Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
0 0
-1000 -1000
1000 1000"""
        output = """Yes
No
No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 4
3 2
6 -1
1 6
6 5
-2 -3
5 3
2 -3
2 1
2 6"""
        output = """Yes
No
No
Yes
Yes
Yes
Yes
Yes
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
