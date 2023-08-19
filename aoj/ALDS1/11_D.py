# 11_D.py

class Graph:

    class Node:
        def __init__(self):
            self.adjs = []
            self.group = None

        def __repr__(self):
            return f"{self.group:3d} {self.adjs}"

    def __init__(self, n):
        self.nodes = [Graph.Node() for _ in range(n)]
        
    @classmethod
    def read(cls, n, m):
        g = Graph(n)
        for _ in range(m):
            s, t = [int(e) for e in input().split()]
            g.nodes[s].adjs.append(t)
            g.nodes[t].adjs.append(s)
        return g

    def find_friends(self, n, group):
        self.nodes[n].group = group
        for adj in self.nodes[n].adjs:
            if self.nodes[adj].group is None:
                self.find_friends(adj, group)

    def groupify(self):
        for n in range(len(self.nodes)):
            if self.nodes[n].group is None:
                self.find_friends(n, n)

    def in_group(self, s, t):
        return self.nodes[s].group == self.nodes[t].group

import sys
sys.setrecursionlimit(200000)

n, m = [int(e) for e in input().split()]
g = Graph.read(n, m)
g.groupify()

q = int(input())
for _ in range(q):
    s, t = [int(e) for e in input().split()]
    print("yes" if g.in_group(s, t) else "no")

