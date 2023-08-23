import sys

moves = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def surround(f, c):
    g = [[c] * (len(f[0]) + 2)]
    for row in f:
        g.append([c] + row + [c])
    g.append([c] * (len(f[0]) + 2))
    return g


def dfs(x, y):
    F[x][y] = "."
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if F[nx][ny] == "W":
            dfs(nx, ny)


N, M = [int(e) for e in sys.stdin.readline().split()]
F = surround([list(sys.stdin.readline().strip()) for _ in range(N)], ".")

ponds = 0
for row in range(N):
    for col in range(M):
        if F[row + 1][col + 1] == "W":
            dfs(row + 1, col + 1)
            ponds += 1
print(ponds)
