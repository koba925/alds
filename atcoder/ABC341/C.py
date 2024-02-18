def resolve_contest():
    dr = {"L": 0, "R": 0, "U": -1, "D": 1}
    dc = {"L": -1, "R": 1, "U": 0, "D": 0}

    def make_pat(T):
        row, col, rows, cols = 0, 0, [0], [0]
        for t in T:
            row += dr[t]
            col += dc[t]
            rows.append(row)
            cols.append(col)
        top, left = min(rows), min(cols)
        h = max(rows) - top + 1
        w = max(cols) - left + 1

        P = [["#"] * w for _ in range(h)]
        for row, col in zip(rows, cols):
            P[row - top][col - left] = "."

        return P

    def can_move(S, P, top, left):
        for row in range(len(P)):
            for col in range(len(P[0])):
                if P[row][col] == "." and S[top + row][left + col] == "#":
                    return False
        return True

    H, W, N = [int(e) for e in input().split()]
    T = input()
    S = [input() for _ in range(H)]

    P = make_pat(T)

    ans = 0
    for top in range(H - len(P) + 1):
        for left in range(W - len(P[0]) + 1):
            if can_move(S, P, top, left):
                ans += 1
    
    print(ans)

def resolve_TLE():
    dr = {"L": 0, "R": 0, "U": -1, "D": 1}
    dc = {"L": -1, "R": 1, "U": 0, "D": 0}

    def can_move(S, row, col):
        if S[row][col] == "#": return False
        for t in T:
            row += dr[t]
            col += dc[t]
            if S[row][col] == "#": return False
        return True
    
    H, W, N = [int(e) for e in input().split()]
    T = input()
    S = [input() for _ in range(H)]

    ans = 0
    for row in range(H):
        for col in range(W):
            if S[row][col] == "." and can_move(S, row, col):
                ans += 1
    
    print(ans)

def resolve_DP_slow():
    DR = {"L": 0, "R": 0, "U": -1, "D": 1}
    DC = {"L": -1, "R": 1, "U": 0, "D": 0}

    H, W, N = [int(e) for e in input().split()]
    T = input()
    S = [[s == "." for s in input()] for _ in range(H)]
    memo = [row[:] for row in S]

    for i in range(N):
        dr, dc = DR[T[i]], DC[T[i]]
        memo2 = [[False] * W for _ in range(H)]
        for r in range(H):
            for c in range(W):
                memo2[(r + dr) % H][(c + dc) % W] = memo[r][c]
        for r in range(H):
            for c in range(W):
                memo2[r][c] = memo2[r][c] and S[r][c]
        memo = memo2

    print(sum(sum(row) for row in memo))                   

def resolve():
    H, W, N = [int(e) for e in input().split()]
    T = input()
    S = sum([[s == "." for s in input()] for _ in range(H)], [])

    memo = S[:]

    for i in range(N):
        match T[i]:
            case "L": memo = memo[1:] + [False]
            case "R": memo = [False] + memo[:-1]
            case "U": memo = memo[W:] + [False] * W
            case "D": memo = [False] * W + memo[:-W]
        memo = [memo[j] and S[j] for j in range(H * W)]

    print(sum(memo))                   

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
        input = """6 7 5
LULDR
#######
#...#.#
##...##
#.#...#
#...#.#
#######"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """13 16 9
ULURDLURD
################
##..##.#..####.#
###.#..#.....#.#
#..##..#####.###
#...#..#......##
###.##.#..#....#
##.#####....##.#
###.###.#.#.#..#
######.....##..#
#...#.#.######.#
##..###..#..#.##
#...#.#.#...#..#
################"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
