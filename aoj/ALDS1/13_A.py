# 13_A.py

WIDTH = 8
queens = set()

def print_board():
    for r in range(WIDTH):
        for c in range(WIDTH):
            print("Q" if (r, c) in queens else ".", end="")
        print()

def captured(row, col):
    for r, c in queens:
        if row == r or col == c or abs(row - r) == abs(col - c):
            return True
    return False

def next_position(row, col):
    return (row + 1) % WIDTH, col + 1 if (row + 1) % WIDTH == 0 else col
    
def search(nth, row, col):
    if nth == WIDTH:
        print_board()
        exit(0)
    elif col == WIDTH:
        return

    if not captured(row, col) and (row, col) not in queens:
        queens.add((row, col))
        search(nth + 1, *next_position(row, col))
        queens.remove((row, col))
    search(nth, *next_position(row, col))

from sys import stdin

k = int(input())
for line in stdin.readlines():
    row, col = [int(e) for e in line.split()]
    queens.add((row, col))
search(k, 0, 0)
