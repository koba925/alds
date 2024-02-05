def resolve_debug_TLE():
    import collections as cl

    N = int(input())
    S = [list(input()) for _ in range(N)]

    drowcol = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def find_players():
        players = []
        for row in range(N):
            for col in range(N):
                if S[row][col] == "P":
                    players.append((row, col))
                    S[row][col] = "."
        return tuple(players)

    def move_players(players, drow, dcol):
        next_players = []
        for row, col in players:
            next_row = max(0, min(N - 1, row + drow))
            next_col = max(0, min(N - 1, col + dcol))
            if S[next_row][next_col] == ".":
                next_players.append((next_row, next_col))
            else:
                next_players.append((row, col))
        return tuple(next_players)
    
    def debug(*args, **kwargs):
        print(*args, **kwargs, file=sys.stderr)

    def bfs(players):
        nonlocal visited
        q = cl.deque()
        q.append((0, players))
        visited[players] = (0, None)

        while q:
            ops, players = q.popleft()
            # debug(ops, players)
            if players[0] == players[1]: return ops, players
            for drow, dcol in drowcol:
                next_players = move_players(players, drow, dcol)
                if next_players != players and next_players not in visited:
                    visited[next_players] = (ops, players)
                    q.append((ops + 1, next_players))

        return -1, None

    visited = {}
    ops, players = bfs(find_players())
    print(ops)
    # while players:
    #     debug(ops, players)
    #     ops, players = visited[players]

def resolve_array_slower():
    import collections as cl

    N = int(input())
    S = [list(input()) for _ in range(N)]

    drowcol = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def find_players():
        P = []
        for row in range(N):
            for col in range(N):
                if S[row][col] == "P":
                    P.append((row, col))
                    S[row][col] = "."
        return tuple(P)

    def move_players(P, drow, dcol):
        NP = []
        for row, col in P:
            nrow = max(0, min(N - 1, row + drow))
            ncol = max(0, min(N - 1, col + dcol))
            if S[nrow][ncol] == ".":
                NP.append((nrow, ncol))
            else:
                NP.append((row, col))
        return tuple(NP)

    def bfs(P):
        q = cl.deque()
        q.append((0, P))
        visited = [[[[False] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
        visited[P[0][0]][P[0][1]][P[1][0]][P[1][1]] = True

        while q:
            ops, P = q.popleft()
            if P[0] == P[1]: return ops
            for drow, dcol in drowcol:
                NP = move_players(P, drow, dcol)
                if NP != P and NP not in visited:
                    visited[NP[0][0]][NP[0][1]][NP[1][0]][NP[1][1]] = True
                    q.append((ops + 1, NP))

        return -1

    print(bfs(find_players()))

def resolve_build_graph_array_TLE():
    import collections as cl

    N = int(input())
    S = [list(input()) for _ in range(N)]

    drowcol = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def find_players():
        P = []
        for row in range(N):
            for col in range(N):
                if S[row][col] == "P":
                    P.append((row, col))
                    S[row][col] = "."
        return (P[0][0], P[0][1], P[1][0], P[1][1])

    def build_graph():
        G = [[[[[] for _ in range(N)] for _ in range(N)] for _ in range(N)] for _ in range(N)]
        for row1 in range(N):
            for col1 in range(N):
                for row2 in range(N):
                    for col2 in range(N):
                        for drow, dcol in drowcol:
                            nrow1 = max(0, min(N - 1, row1 + drow))
                            ncol1 = max(0, min(N - 1, col1 + dcol))
                            if S[nrow1][ncol1] == "#": nrow1, ncol1 = row1, col1
                            nrow2 = max(0, min(N - 1, row2 + drow))
                            ncol2 = max(0, min(N - 1, col2 + dcol))
                            if S[nrow2][ncol2] == "#": nrow2, ncol2 = row2, col2
                            if nrow1 != row1 or ncol1 != col1 or nrow2 != row2 or ncol2 != col2:
                                G[row1][col1][row2][col2].append((nrow1, ncol1, nrow2, ncol2))
        return G

    def bfs(P):
        q = cl.deque()
        q.append((0, P))
        visited = [[[[False] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]
        visited[P[0]][P[1]][P[2]][P[3]] = True

        while q:
            ops, P = q.popleft()
            if P[0] == P[2] and P[1] == P[3]: return ops
            for NP in G[P[0]][P[1]][P[2]][P[3]]:
                if not visited[NP[0]][NP[1]][NP[2]][NP[3]]:
                    visited[NP[0]][NP[1]][NP[2]][NP[3]] = True
                    q.append((ops + 1, NP))

        return -1

    G = build_graph()
    print(bfs(find_players()))


def resolve_build_graph_set_TLE():
    import collections as cl

    N = int(input())
    S = [list(input()) for _ in range(N)]

    drowcol = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    
    def find_players():
        P = []
        for row in range(N):
            for col in range(N):
                if S[row][col] == "P":
                    P += [row, col]
                    S[row][col] = "."
        return tuple(P)

    def build_graph():
        G = cl.defaultdict(lambda: [])
        for row1 in range(N):
            for col1 in range(N):
                for row2 in range(N):
                    for col2 in range(N):
                        for drow, dcol in drowcol:
                            nrow1 = max(0, min(N - 1, row1 + drow))
                            ncol1 = max(0, min(N - 1, col1 + dcol))
                            if S[nrow1][ncol1] == "#": nrow1, ncol1 = row1, col1
                            nrow2 = max(0, min(N - 1, row2 + drow))
                            ncol2 = max(0, min(N - 1, col2 + dcol))
                            if S[nrow2][ncol2] == "#": nrow2, ncol2 = row2, col2
                            if nrow1 != row1 or ncol1 != col1 or nrow2 != row2 or ncol2 != col2:
                                G[(row1, col1, row2, col2)].append((nrow1, ncol1, nrow2, ncol2))
        return G

    def bfs(P):
        q = cl.deque()
        q.append((0, P))
        visited = set([P])

        while q:
            ops, P = q.popleft()
            if P[0] == P[2] and P[1] == P[3]: return ops
            for NP in G[P]:
                if NP not in visited:
                    visited.add(NP)
                    q.append((ops + 1, NP))

        return -1

    G = build_graph()
    print(bfs(find_players()))

def resolve_selfhash_AC():
    import collections as cl

    def solve(N, S):
        P = []
        for row in range(N):
            for col in range(N):
                if S[row][col] == "P":
                    P += [row, col]
                    S[row][col] = "."
        P = tuple(P)

        q = cl.deque()
        q.append(P)
        row1, col1, row2, col2 = P
        visited = set([row1 * 1000000 + col1 * 10000 + row2 * 100 + col2])

        ops = 0
        while q:
            for _ in range(len(q)):
                P = q.popleft()
                row1, col1, row2, col2 = P
                if row1 == row2 and col1 == col2: return ops
                for drow, dcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nrow1 = max(0, min(N - 1, row1 + drow))
                    ncol1 = max(0, min(N - 1, col1 + dcol))
                    if S[nrow1][ncol1] == "#": nrow1, ncol1 = row1, col1
                    nrow2 = max(0, min(N - 1, row2 + drow))
                    ncol2 = max(0, min(N - 1, col2 + dcol))
                    if S[nrow2][ncol2] == "#": nrow2, ncol2 = row2, col2
                    NP = (nrow1, ncol1, nrow2, ncol2)
                    if NP == P: continue
                    hash = nrow1 * 1000000 + ncol1 * 10000 + nrow2 * 100 + ncol2
                    if hash not in visited:
                        visited.add(hash)
                        q.append(NP)
            ops += 1
        return -1

    N = int(input())
    S = [list(input()) for _ in range(N)]

    print(solve(N, S))


def resolve():
    import collections as cl

    def solve(N, S):
        P = []
        for row in range(N):
            for col in range(N):
                if S[row][col] == "P":
                    P += [row, col]
                    S[row][col] = "."
        P = tuple(P)

        q = cl.deque()
        q.append(P)
        row1, col1, row2, col2 = P
        visited = set([row1 * 1000000 + col1 * 10000 + row2 * 100 + col2])

        ops = 0
        while q:
            for _ in range(len(q)):
                P = q.popleft()
                row1, col1, row2, col2 = P
                if row1 == row2 and col1 == col2: return ops
                for drow, dcol in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    nrow1 = row1 + drow
                    ncol1 = col1 + dcol
                    if S[nrow1][ncol1] == "#": nrow1, ncol1 = row1, col1
                    nrow2 = row2 + drow
                    ncol2 = col2 + dcol
                    if S[nrow2][ncol2] == "#": nrow2, ncol2 = row2, col2
                    NP = (nrow1, ncol1, nrow2, ncol2)
                    if NP == P: continue
                    hash = nrow1 * 1000000 + ncol1 * 10000 + nrow2 * 100 + ncol2
                    if hash not in visited:
                        visited.add(hash)
                        q.append(NP)
            ops += 1
        return -1

    N = int(input())
    S = [list("#" * (N + 2))]
    S += [["#"] + list(input()) + ["#"] for _ in range(N)]
    S += [list("#" * (N + 2))]

    print(solve(N + 2, S))

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
        input = """5
....#
#..#.
.P...
..P..
....#"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
P#
#P"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
..........
..........
..........
..........
....P.....
.....P....
..........
..........
..........
.........."""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
