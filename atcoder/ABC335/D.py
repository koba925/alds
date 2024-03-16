N = int(input())

G = [["_"] * N for _ in range(N)]
tr = tc =  (N + 1) // 2 - 1
G[tr][tc] = "T"

p = 1
for i in range(1, (N - 1) // 2 + 1):
    for r in range(tr - i + 1, tr + i + 1):
        G[r][tc - i] = str(p)
        p += 1
    for c in range(tc - i + 1, tc + i + 1):
        G[tr + i][c] = str(p)
        p += 1
    for r in range(tr + i - 1, tr - i - 1, -1):
        G[r][tc + i] = str(p)
        p += 1
    for c in range(tc + i - 1, tc - i - 1, -1):
        G[tr - i][c] = str(p)
        p += 1

for row in G:
    print(*row)

