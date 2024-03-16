import sys
from io import StringIO
import unittest

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
    
    N, M = [int(e) for e in input().split()]
    group = UnionFind(N)
    for _ in range(M):
        a, b = [int(e) for e in input().split()]
        group.unite(a - 1, b - 1)

    print(M - N + group.num_sets())

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """6 7
1 2
1 3
2 3
4 2
6 5
4 6
4 5"""
        expected = """2"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """4 2
1 2
3 4"""
        expected = """0"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """5 3
1 2
1 3
2 3"""
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
