# 13_C.py 15 Puzzle
# TODO
# 13_B code: #15 8.29 #17 13.01
# A* Simple heuristics: #15 0.03s #17 4.53s
# A* Manhattan heuristics: #15 0.01s #17 0.11s #20 0.76s #21 11.71 #22 TLE
# A* Rolling Hash: #15 0.01s #17 0.11s #20 0.73s #21 11.25 #22 TLE
# A* Rolling Manhattan: AC #15 0.01s #17 0.02s #20 0.05s #21 1.53s #22 0.91s #28 3.90s
# IDA*: AC #15 0.01s #17 0.01s #20 0.07s #21 3.52s #22 2.32s #28 5.67s

from sys import stdin

LIMIT = 45
GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

def neighbors(pos):
    if pos >= 4:
        yield pos - 4
    if pos < 12:
        yield pos + 4
    if pos % 4 != 0:
        yield pos - 1
    if pos % 4 != 3:
        yield pos + 1

NEIGHBORS = [list(neighbors(pos)) for pos in range(16)]

def swap(board, pos, new_pos):
    new_board = board[:]
    new_board[pos], new_board[new_pos] = new_board[new_pos], new_board[pos]
    return new_board

# Simple heuristics
# def heu(board):
#     return len([1 for b, g in zip(board, GOAL) if b != g])

# Manhattan heuristics
GOAL_POS = [GOAL.index(i) for i in range(16)]
MAN_DIST = [
    [abs(p // 4 - q // 4) + abs(p % 4 - q % 4) for q in range(16)]
    for p in range(16)
]

def heuristics(board):
    return sum([MAN_DIST[board.index(i)][GOAL_POS[i]] for i in range(1, 16)])

def roll_heuristics(heur, board, pos, new_pos):
    return heur - MAN_DIST[new_pos][GOAL_POS[board[new_pos]]] + MAN_DIST[pos][GOAL_POS[board[new_pos]]]

# Rolling Hash
POWER16 = [16 ** i for i in range(16)]

def calc_hash(board):
    return sum([POWER16[i] * board[i] for i in range(16)])

GOAL_HASH = calc_hash(GOAL)

def roll_hash(hash, board, pos, new_pos):
    return hash - board[new_pos] * POWER16[new_pos] + board[new_pos] * POWER16[pos]

def print_board(board):
    for i in range(16):
        print(f"{board[i]:2d} ", end="")
        if i % 4 == 3:
            print()

# A*
# from heapq import heappush, heappop
# def solve(board):
#     visited = set()
#     moves = 0
#     pos = board.index(0)
#     heur = heuristics(board)
#     # print_board(board)
#     # print(heur)
#     hash = calc_hash(board)
#     # print(hex(hash))
#     queue = [(moves + heur, heur, moves, board, hash, pos)]
#
#     while len(queue) > 0:
#         priority, heur, moves, board, hash, pos = heappop(queue)
#         if hash == GOAL_HASH:
#             return moves
#         visited.add(hash)
#
#         for new_pos in NEIGHBORS[pos]:
#             new_hash = roll_hash(hash, board, pos, new_pos)
#             # print(hex(new_hash))
#             if not new_hash in visited:
#                 new_board = swap(board, pos, new_pos)
#                 new_heur = roll_heuristics(heur, board, pos, new_pos)
#                 # print_board(new_board)
#                 # print(new_heur)
#                 heappush(queue, (
#                     moves + new_heur, new_heur, moves + 1, new_board, new_hash, new_pos
#                 ))

# IDA*
def dfs(limit, depth, board, heur, prev_pos, pos):
    if depth + heur > limit:
        return False
    if heur == 0:
        return True

    for new_pos in NEIGHBORS[pos]:
        if new_pos == prev_pos:
            continue
        new_board = swap(board, pos, new_pos)
        new_heur = roll_heuristics(heur, board, pos, new_pos)
        # print_board(new_board)
        # print(new_heur)
        if dfs(limit, depth + 1, new_board, new_heur, pos, new_pos):
            return True

    return None

def solve(board):
    moves = 0
    pos = board.index(0)
    heur = heuristics(board)
    # print_board(board)
    # print(heur)
    for limit in range(heur, LIMIT + 1):
        if dfs(limit, moves, board, heur, -1, pos):
            return limit
    return None

#board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 0, 15]
board = [int(e) for e in stdin.read().split()]
print(solve(board))
