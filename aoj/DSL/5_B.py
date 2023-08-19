# 5_B.py The Maximum Number of Overlaps
# AC 0.72s 64720KB

MAXPOS = 1000

def solve(n, rects):
    coords = [[0] * (MAXPOS + 1) for _ in range(MAXPOS + 1)]
    for x1, y1, x2, y2 in rects:
        coords[y1][x1] += 1
        coords[y1][x2] -= 1
        coords[y2][x1] -= 1
        coords[y2][x2] += 1

    for y in range(MAXPOS):
        for x in range(1, MAXPOS + 1):
            coords[y][x] += coords[y][x - 1]

    for y in range(1, MAXPOS + 1):
        for x in range(MAXPOS):
            coords[y][x] += coords[y - 1][x]

    return max(max(xs) for xs in coords)

from sys import stdin

n = int(stdin.readline())
rects = [[int(e) for e in line.split()] for line in stdin.readlines()]

print(solve(n, rects))

