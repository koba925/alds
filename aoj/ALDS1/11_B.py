# 11_B.py

class Node:
    def __init__(self, vs=[]) -> None:
        self.d = 0
        self.f = 0
        self.vs = vs
        self.vi = 0

    def __repr__(self):
        return f"({self.d} {self.f} {self.vi} {self.vs})"

    def nextv(self):
        if self.vi >= len(self.vs):
            return -1
        val = self.vs[self.vi]
        self.vi += 1
        return val
     
class Graph:
    def __init__(self, n):
        self.n = n
        self.nodes = nodes = [None] * (n + 1)

    def read(self):    
        for _ in range(self.n):
            u, k, *vs = [int(e) for e in input().split()]
            self.nodes[u] = Node(vs)

    def print(self):
        for u in range(1, self.n + 1):
            print(u, self.nodes[u].d, self.nodes[u].f)

    def dfs_stack(self, u, t):
        waiting = [u]
        self.nodes[u].d = t
        t += 1
        while len(waiting) > 0:
            u = waiting[-1]
            v = self.nodes[u].nextv()
            if v == -1:
                self.nodes[u].f = t
                t += 1
                waiting.pop()
            elif self.nodes[v].d == 0:
                self.nodes[v].d = t
                t += 1
                waiting.append(v)
        return t - 1
                    
    def dfs(self, u, t):
        self.nodes[u].d = t
        for v in self.nodes[u].vs:
            if self.nodes[v].d == 0:
                t = self.dfs(v, t + 1)
        self.nodes[u].f = t + 1
        return self.nodes[u].f

    def dfs_all(self):
        t = 1
        for u in range(1, self.n + 1):
            if self.nodes[u].d == 0:
                t = self.dfs_stack(u, t) + 1

g = Graph(int(input()))
g.read()
g.dfs_all()
g.print()
