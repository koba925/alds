def resolve_TLE():
    import sys
    sys.setrecursionlimit(2000000)

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
                return False
    
            # union by size
            if self._elems[x] < self._elems[y]:
                x, y = y, x
            self._parent[y] = x
            self._elems[x] += self._elems[y]
            return True
            
        def same(self, x, y):    
            return self._ancestor(x) == self._ancestor(y)
        
        def num_sets(self):
            return len([1 for i in range(self.size) if self._parent[i] == i])
        
    def spanning():
        uf = UnionFind(N)
        for i in range(M):
            if used[i]:
                uf.unite(E[i][0], E[i][1])        
        return uf.num_sets() == 1

    def dfs(weight):
        nonlocal min_cost

        if spanning():
            min_cost = min(min_cost, weight % K)
            return
        
        for e in range(M):
            if used[e]: continue
            used[e] = True
            if not visited[E[e][0]] or not visited[E[e][1]]:
                v1, v2 = visited[E[e][0]], visited[E[e][1]]
                visited[E[e][0]] = visited[E[e][1]] = True
                dfs(weight + E[e][2])
                visited[E[e][0]], visited[E[e][1]] = v1, v2
            used[e] = False

    N, M, K = [int(e) for e in input().split()]
    E = [] 
    for _ in range(M):
        u, v, w = [int(e) for e in input().split()]
        E.append((u - 1, v - 1, w))

    min_cost = float("inf")
    visited = [False] * N
    used = [False] * M

    for e in range(M):
        used[e] = visited[E[e][0]] = visited[E[e][1]] = True
        dfs(E[e][2])
        used[e] = visited[E[e][0]] = visited[E[e][1]] = False

    print(min_cost)

def resolve():
    class UnionFind:
        def __init__(self, size):
            self._size = size
            self._parent = list(range(size))
            self._elems = [1] * size
    
        def _ancestor(self, x):
            while self._parent[x] != x:
                x = self._parent[x]
            return x
    
        def unite(self, x, y):
            x, y = self._ancestor(x), self._ancestor(y)
            if x == y: return False # if x and y are in the same group
            if self._elems[x] < self._elems[y]: x, y = y, x
            self._parent[y] = x
            self._elems[x] += self._elems[y]
            return True
            
        def same(self, x, y):    
            return self._ancestor(x) == self._ancestor(y)
        
        def num_sets(self):
            return len([1 for i in range(self._size) if self._parent[i] == i])
        
    import itertools as it

    N, M, K = [int(e) for e in input().split()]
    E = [] 
    for _ in range(M):
        u, v, w = [int(e) for e in input().split()]
        E.append((u - 1, v - 1, w))

    min_cost = float("inf")
    for c in it.combinations(range(M), N - 1):
        weight, group = 0, UnionFind(N)
        for e in c:
            if not group.unite(E[e][0], E[e][1]):
                break
            weight += E[e][2]
        else:
            min_cost = min(min_cost, weight % K)

    print(min_cost)
    

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
        input = """5 6 328
1 2 99
1 3 102
2 3 86
2 4 94
2 5 95
3 4 81"""
        output = """33"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5 998244353
1 2 337361568
1 6 450343304
2 3 61477244
2 5 745383438
4 5 727360840"""
        output = """325437688"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 28 936294041850197
1 2 473294720906780
1 3 743030800139244
1 4 709363019414774
1 5 383643612490312
1 6 557102781022861
1 7 623179288538138
1 8 739618599410809
2 3 857687812294404
2 4 893923168139714
2 5 581822471860662
2 6 740549363586558
2 7 307226438833222
2 8 447399029952998
3 4 636318083622768
3 5 44548707643622
3 6 307262781240755
3 7 12070267388230
3 8 700247263184082
4 5 560567890325333
4 6 704726113717147
4 7 588263818615687
4 8 549007536393172
5 6 779230871080408
5 7 825982583786498
5 8 713928998174272
6 7 751331074538826
6 8 449873635430228
7 8 11298381761479"""
        output = """11360716373"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
