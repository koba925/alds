# 2_B.py Chinese Postman Problem

# 単純なDFSでは探索が終わらない 打ち切る必要あり
# IDA*か？最短の保証はできる？
def postman(adjs):
    return 0
    
def solve(v, e, edges):
    adjs = [[] for _ in range(v)]
    for i in range(e):
        s, t, d = edges[i]
        edges[i].append(False)
        adjs[s].append((t, d, i))
        adjs[t].append((s, d, i))

    print(postman(edges, adjs))

# solve(4, 6, [[0, 1, 2], [1, 2, 3], [1, 3, 9], [2, 0, 1], [2, 3, 6], [3, 2, 4]])
# exit()

from sys import stdin

v, e = [int(e) for e in stdin.readline().split()]
edges = [[int(e) for e in line.split()] for line in stdin.readlines()]
solve(v, e, edges)