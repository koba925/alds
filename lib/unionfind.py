class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def ancestor(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        return x

    def unite(self, x, y):
        x = self.ancestor(x)
        y = self.ancestor(y)

        if x == y:
            return

        # union by size
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]

    def same(self, x, y):    
        return self.ancestor(x) == self.ancestor(y)
    
class WeightedUnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.diff_weight = [0] * n
        self.size = [1] * n         # union by size

    # no route compression
    # AC 01.03 s 27376 KB
    def ancestor_weight(self, x):
        weight = 0
        while self.parent[x] != x:
            weight += self.diff_weight[x]
            x = self.parent[x]
        return x, weight

    # route compression
    # AC 01.03 s 27376 KB
    # def ancestor_weight(self, x):
    #     if self.parent[x] == x:
    #         return x, 0

    #     ancestor, weight = self.ancestor_weight(self.parent[x])
    #     self.parent[x] = ancestor
    #     self.diff_weight[x] += weight
    #     return ancestor, self.diff_weight[x]

    def relate(self, x, y, z):
        xa, xw = self.ancestor_weight(x)
        ya, yw = self.ancestor_weight(y)

        if xa == ya:
            return

        w = yw + z - xw 
        if self.size[xa] > self.size[ya]:
            xa, ya = ya, xa
            w *= -1
        self.parent[xa] = ya
        self.size[ya] += self.size[xa]
        self.diff_weight[xa] = w
    
    def difference_between(self, x, y):    
        xa, xd = self.ancestor_weight(x)
        ya, yd = self.ancestor_weight(y)
        return None if xa != ya else xd - yd
