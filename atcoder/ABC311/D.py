import sys
from collections import deque

sys.setrecursionlimit(2000000)

def grid_ice_floor_mine(N, M, S):
    def state(pos):
        return S[pos[0]][pos[1]]
    
    def set_state(pos, s):
        S[pos[0]][pos[1]] = s

    def new_pos(pos, move):
        return [pos[0] + move[0], pos[1] + move[1]]

    def go(start, move):
        nonlocal S

        set_state(start, "s")
        pos = start[:]
        while state(new_pos(pos, move)) != "#":
            pos = new_pos(pos, move)
            if state(pos) == ".":
                set_state(pos, "p")
        return pos
    
    def bfs(start):
        nonlocal S

        q = deque()
        q.append(start)
        while q:
            pos = q.popleft()
            for move in moves:
                stop = go(pos, move)
                if state(stop) != "s":
                    q.append(stop)

    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    bfs([1, 1])
    return sum(len([1 for s in Si if s in ("ps")]) for Si in S)

def grid_ice_floor_editorial(N, M, S):
    def go(r, c, dr, dc):
        passed[r][c] = stopped[r][c] = True
        while S[r + dr][c + dc] != "#":
            r, c = r + dr, c + dc
            passed[r][c] = True
        return r, c
    
    def dfs(r, c):
        for dr, dc in moves:
            nr, nc = go(r, c, dr, dc)
            if not stopped[nr][nc]:
                dfs(nr, nc)

    moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    passed = [[False] * M for _ in range(N)]
    stopped = [[False] * M for _ in range(N)]
    dfs(1, 1)
    return sum(sum(row) for row in passed)

def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    S = [list(sys.stdin.readline().strip()) for _ in range(N)]
    # print(grid_ice_floor_mine(N, M, S))
    print(grid_ice_floor_editorial(N, M, S))

# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """6 6
######
#....#
#.#..#
#..#.#
#....#
######"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """21 25
#########################
#..............###...####
#..............#..#...###
#........###...#...#...##
#........#..#..#........#
#...##...#..#..#...#....#
#..#..#..###...#..#.....#
#..#..#..#..#..###......#
#..####..#..#...........#
#..#..#..###............#
#..#..#.................#
#........##.............#
#.......#..#............#
#..........#....#.......#
#........###...##....#..#
#..........#..#.#...##..#
#.......#..#....#..#.#..#
##.......##.....#....#..#
###.............#....#..#
####.................#..#
#########################"""
        output = """215"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
