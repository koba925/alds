import sys


def find(field, elem):
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == elem:
                return (row, col)
    return None


import collections as cl

INF = 99


def saitanro(N, M, maze):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    srow, scol = find(maze, "S")
    grow, gcol = find(maze, "G")
    distance = [[INF] * M for _ in range(N)]

    distance[srow][scol] = 0
    que = cl.deque()
    que.appendleft((srow, scol))

    while que:
        row, col = que.pop()
        if row == grow and col == gcol:
            break

        for drow, dcol in moves:
            nrow, ncol = row + drow, col + dcol
            if (
                0 <= nrow < N
                and 0 <= ncol < M
                and maze[nrow][ncol] != "#"
                and distance[nrow][ncol] == INF
            ):
                que.appendleft((nrow, ncol))
                distance[nrow][ncol] = distance[row][col] + 1

    return distance[grow][gcol]


N, M = [int(e) for e in sys.stdin.readline().split()]
maze = [list(sys.stdin.readline().strip()) for _ in range(N)]

print(saitanro(N, M, maze))

"""
10 10
#S######.#
......#..#
.#.##.##.#
.#........
##.##.####
....#....#
.#######.#
....#.....
.####.###.
....#...G#
"""
