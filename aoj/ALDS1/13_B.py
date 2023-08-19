# 13_B.py

# visited check #23 2.65 #20 1.69
# 1-dim tuple #23 0.96 #20 0.59
# 1-dim list #23 0.97 #20 0.56

from collections import deque

def neighbors(pos):
    if pos >= 3:
        yield pos - 3
    if pos < 6:
        yield pos + 3
    if pos % 3 != 0:
        yield pos - 1
    if pos % 3 != 2:
        yield pos + 1

def swap(board, pos, next_pos):
    new_board = board[:]
    new_board[pos], new_board[next_pos] = new_board[next_pos], new_board[pos]
    return new_board

def solve(board):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    visited = set()
    moves = 0
    pos = board.index(0)
    queue = deque([(moves, board, pos)])

    while len(queue) > 0:
        moves, board, pos = queue.popleft()
        if board == goal:
            return moves
        visited.add(tuple(board))

        for next_pos in neighbors(pos):
            new_board = swap(board, pos, next_pos)
            if not tuple(new_board) in visited:
                queue.append((moves + 1, new_board, next_pos))

from sys import stdin

board = [int(e) for e in stdin.read().split()]
print(solve(board))
