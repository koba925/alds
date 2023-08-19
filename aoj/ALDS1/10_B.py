# 10_B.py

from math import inf


def chain_matrix(M):

    n = len(M)
    T = [[inf] * n for _ in range(n)]

    for i in range(n):
        T[i][i] = 0

    for width in range(1, n):
        for l in range(0, n - width):
            r = l + width
            T[l][r] = min([
                T[l][m] + T[m + 1][r] + M[l][0] * M[m][1] * M[r][1]
                for m in range(l, r)
            ])

    return T[0][len(M) - 1]


n = int(input())

s = 0
M = []
for _ in range(n):
    M.append([int(e) for e in input().split()])

print(chain_matrix(M))
