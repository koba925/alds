# 1_A.py Disjoint Set: Union Find Tree

class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        # self.height = [0] * n
        self.size = [1] * n

    # 0.42s 13960KB
    def ancestor(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    # 0.44s 13960KB
    # def ancestor(self, x):
    #     if self.parent[x] == x:
    #         return x
    #     self.parent[x] = self.ancestor(self.parent[x])
    #     return self.parent[x]

    # 0.49s 13960KB
    # def ancestor(self, x):
    #     a = x
    #     while self.parent[a] != a:
    #         a = self.parent[a]
    #     while self.parent[x] != x:
    #         x, self.parent[x] = self.parent[x], a
    #     return a

    def unite(self, x, y):
        x = self.ancestor(x)
        y = self.ancestor(y)

        if x == y:
            return

        # union by size 0.42s 13868KB
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]

        # union by rank 0.42s 13960KB
        # if self.height[x] < self.height[y]:
        #     self.parent[x] = y
        # else:
        #     self.parent[y] = x 
        #     if self.height[x] == self.height[y]:
        #         self.height[x] += 1

    def same(self, x, y):    
        return self.ancestor(x) == self.ancestor(y)

from sys import stdin

n, q = [int(e) for e in stdin.readline().split()]

uft = UnionFind(n)
for line in stdin.readlines():
    com, *param = [int(e) for e in line.split()]
    if com == 0:
        uft.unite(param[0], param[1])
    elif com == 1:
        print(1 if uft.same(param[0], param[1]) else 0)
