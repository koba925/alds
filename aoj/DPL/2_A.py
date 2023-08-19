# 2_A.py Traveling Salesman Problem

from sys import stdin
INF = 10 ** 10

# exhaustive search #27 TLE #26 1.49s 5620KB
# def salesman(adjs):
#
#     def _salesman(i, rest_verts):
#         if not rest_verts:
#             return 0
#
#         min_dist = INF
#         for next_vert, next_dist in adjs[i]:
#             if next_vert not in rest_verts:
#                 continue
#             if next_vert != 0 or len(rest_verts) == 1:
#                 next_rests = rest_verts.copy()
#                 next_rests.remove(next_vert)
#                 min_dist = min(min_dist, next_dist +_salesman(next_vert, next_rests))
#         return min_dist
#
#     return _salesman(0, set(range(len(adjs))))

# memoize: AC 1.65s 93792KB #26 0.03s 6816KB
# def salesman(adjs):
#
#     def _salesman(i, rest_verts):
#         rv = frozenset(rest_verts)
#         if (i, rv) in memo:
#             return memo[(i, rv)]
#
#         min_dist = INF
#         if not rest_verts:
#             min_dist = 0
#         else:
#             for next_vert, next_dist in adjs[i]:
#                 if next_vert not in rest_verts:
#                     continue
#                 if next_vert != 0 or len(rest_verts) == 1:
#                     next_rests = rest_verts.copy()
#                     next_rests.remove(next_vert)
#                     min_dist = min(min_dist, next_dist +_salesman(next_vert, next_rests))
#         memo[(i, rv)] = min_dist
#         return min_dist
#
#     memo = {}
#     return _salesman(0, set(range(len(adjs))))

# own hash: AC 2.46s 13096
# def salesman(adjs):
#
#     def hash(rest_verts):
#         h = 0
#         for v in rest_verts:
#             h += 2 ** v
#         return h
#
#     def _salesman(i, rest_verts):
#         h = hash(rest_verts)
#         if memo[i][h] is not None:
#             return memo[i][h]
#
#         min_dist = INF
#         if not rest_verts:
#             min_dist = 0
#         else:
#             for next_vert, next_dist in adjs[i]:
#                 if next_vert not in rest_verts:
#                     continue
#                 if next_vert != 0 or len(rest_verts) == 1:
#                     next_rests = rest_verts.copy()
#                     next_rests.remove(next_vert)
#                     min_dist = min(min_dist, next_dist +_salesman(next_vert, next_rests))
#         memo[i][h] = min_dist
#         return min_dist
#
#     memo = [[None] * (2 ** len(adjs)) for _ in range(len(adjs))]
#     return _salesman(0, set(range(len(adjs))))

# DP from goal: AC 1.79s 15456KB
# def salesman(adjs):
#     alen = len(adjs)
#     memo = [[INF] * alen for _ in range(2 ** alen)]
#     START = 2 ** alen - 1
#     memo[0][0] = 0

#     for h in range(1, 2 ** alen):
#         for i in range(alen):
#             if h >> i & 1 == 1 and h != START:
#                 continue
#             for next_vert, next_dist in adjs[i]:
#                 if h >> next_vert & 1 == 0:
#                     continue
#                 memo[h][i] = min(
#                     memo[h][i],
#                     next_dist + memo[h - 2 ** next_vert][next_vert])

#     return memo[-1][0]

# DP from start: AC 2.20s 19804KB
# def salesman(adjs):
#     alen = len(adjs)
#     memo = [[INF] * alen for _ in range(2 ** alen)]
#     memo[0][0] = 0
#
#     for h in range(2 ** alen):
#         for i in range(alen):
#             if memo[h][i] == INF:
#                 continue
#             for next_vert, next_dist in adjs[i]:
#                 if h >> next_vert & 1 == 1:
#                     continue
#                 memo[h + 2 ** next_vert][next_vert] = min(
#                     memo[h + 2 ** next_vert][next_vert],
#                     next_dist + memo[h][i]
#                 )
#                
#     return memo[-1][0]

# memoize by bits & dict: 1.75s 42844KB
def salesman(adjs):

    def _salesman(i, rest_verts):
        if (i, rest_verts) in memo:
            return memo[(i, rest_verts)]

        if rest_verts == 0:
            min_dist = 0 if i == 0 else INF
        else:
            min_dist = INF
            for next_vert, next_dist in adjs[i]:
                if  rest_verts >> next_vert & 1 == 0:
                    continue
                next_rests = rest_verts - (1 << next_vert)
                min_dist = min(min_dist, next_dist + _salesman(next_vert, next_rests))
        memo[(i, rest_verts)] = min_dist
        return min_dist

    memo = {}
    return _salesman(0, 2 ** len(adjs) - 1)

def solve(v, e, edges):
    adjs = [[] for _ in range(v)]
    for s, t, d in edges:
        adjs[s].append((t, d))

    mind = salesman(adjs)
    print(mind if mind < INF else -1)


# solve(4, 6, [[0, 1, 2], [1, 2, 3], [1, 3, 9], [2, 0, 1], [2, 3, 6], [3, 2, 4]])
# exit()

v, e = [int(e) for e in stdin.readline().split()]
edges = [[int(e) for e in line.split()] for line in stdin.readlines()]
solve(v, e, edges)
