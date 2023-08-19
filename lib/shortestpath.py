# shortestpath.py 単一始点採点経路 ダイクストラ Dijkstra

from heapq import heappush, heappop
from collections import namedtuple
from math import inf

Adj = namedtuple("Adj", "id, wgt")

class Vert:
    def __init__(self, adjs):
        self.parent = None
        self.visited = False
        self.distance = inf
        self.adjs = adjs

    def __repr__(self):
        return f"Vert({self.parent}, {self.visited}, {self.distance}, {self.adjs})"


class Graph:
    def __init__(self, n, adjs) -> None:
        self.n = n
        self.verts = [Vert(adjs[id]) for id in range(n)]

    def shortest_path(self, start):

        hq = []

        self.verts[start].distance = 0
        heappush(hq, (0, start))

        while len(hq) > 0:
            nearest_dist, nearest_id = heappop(hq)

            nearest = self.verts[nearest_id]
            if nearest.visited:
                continue
            nearest.visited = True

            for adj in nearest.adjs:
                nextv = self.verts[adj.id]
                if (not nextv.visited and
                        nearest.distance + adj.wgt < nextv.distance):
                    nextv.distance = nearest.distance + adj.wgt
                    nextv.parent = nearest_id
                    heappush(hq, (nextv.distance, adj.id))

    def distances(self):
        for i in range(self.n):
            yield self.verts[i].distance


n = int(input())
adjs = [None] * n
for _ in range(n):
    id, _, *tmp = [int(e) for e in input().split()]
    adjs[id] = [Adj(id, wgt) for id, wgt in zip(tmp[::2], tmp[1::2])]

g = Graph(n, adjs)
g.shortest_path(0)

for i, d in enumerate(g.distances()):
    print(i, d)
