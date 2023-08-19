import sys

sys.setrecursionlimit(2000000)

def divceil(a, x): return -(-a // x)

def distance_sq(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

def on_circle(p, c):
    return distance_sq(p, c) == c[2] ** 2

def find_circle(p, C):
    for i, c in enumerate(C):
        if on_circle(p, c):
            return i
 
def crossing(c1, c2):
    d = distance_sq(c1, c2)
    return abs(c1[2] - c2[2]) ** 2 <= distance_sq(c1, c2) <= (c1[2] + c2[2]) ** 2

def circle_graph(C):
    l = len(C)
    adj = [[] for _ in range(l)]
    for i in range(l):
        for j in range(i + 1, l):
            if crossing(C[i], C[j]):
                adj[i].append(j)
                adj[j].append(i)
    return adj

    
def can_reach(N, S, T, C):
    # TLE
    def dfs_rec(n):
        if n == t:
            return True
        visited.add(n)
        for a in adj[n]:
            if a not in visited and dfs_rec(a):
                return True
        return False

    def dfs():
        nonlocal visited

        stack = []
        stack.append(s)

        while stack:
            v = stack.pop()
            visited.add(v)
            if v == t:
                return True
            for a in adj[v]:
                if a not in visited:
                    stack.append(a)

        return False
    
    visited = set()
    s = find_circle(S, C)
    t = find_circle(T, C)
    adj = circle_graph(C)
    return dfs_rec(s)
    # return dfs()

def resolve():
    N = int(sys.stdin.readline())
    sx, sy, tx, ty = [int(e) for e in sys.stdin.readline().split()]
    S, T = (sx, sy), (tx, ty)
    C = [tuple([int(e) for e in line.split()]) for line in sys.stdin.readlines()]

    print("Yes" if can_reach(N, S, T, C) else "No")

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
        input = """4
0 -2 3 3
0 0 2
2 0 2
2 3 1
-3 3 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
0 1 0 3
0 0 1
0 0 2
0 0 3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
