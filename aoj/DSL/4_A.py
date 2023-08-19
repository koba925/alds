# 4_A.py Union of Rectalgles
# AC 9.95s 344152KB

MAXPOS = 2000

def solve(n, rects):
    xs, ys = set(), set()
    for x1, y1, x2, y2 in rects:
        xs.add(x1)
        xs.add(x2)
        ys.add(y1)
        ys.add(y2)

    xs = sorted(xs)
    xslen = len(xs)
    comp2x = dict(zip(range(len(xs)), xs))
    x2comp = dict(zip(xs, range(len(xs))))
    widths = [xs[i + 1] - xs[i] for i in range(xslen - 1)]

    ys = sorted(ys)
    yslen = len(ys)
    comp2y = dict(zip(range(len(ys)), ys))
    y2comp = dict(zip(ys, range(len(ys))))
    heights = [ys[i + 1] - ys[i] for i in range(yslen - 1)]

    coords = [[0] * xslen for _ in range(yslen)]

    for x1, y1, x2, y2 in rects:
        coords[y2comp[y1]][x2comp[x1]] += 1
        coords[y2comp[y1]][x2comp[x2]] -= 1
        coords[y2comp[y2]][x2comp[x1]] -= 1
        coords[y2comp[y2]][x2comp[x2]] += 1

    for y in range(yslen):
        for x in range(1, xslen):
            coords[y][x] += coords[y][x - 1]

    for y in range(1, yslen):
        for x in range(xslen):
            coords[y][x] += coords[y - 1][x]

    area = 0
    for y in range(yslen - 1):
        for x in range(xslen - 1):
            if coords[y][x] > 0:
                area += widths[x] * heights[y] 

    return area

from sys import stdin

n = int(stdin.readline())
rects = [[int(e) for e in line.split()] for line in stdin.readlines()]

print(solve(n, rects))
