# 11_A.py

def read_adj_list(n):
    mat = [[0] * n for _ in range(n)]
    for _ in range(n):
        u, _, *vs = [int(e) for e in input().split()]
        for v in vs:
            mat[u - 1][v - 1] = 1
    return mat

n = int(input())
for r in read_adj_list(n):
    print(*r)
