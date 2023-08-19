# B - Bingo

def bingo(marks):
    for r in range(3):
        if all(marks[r]):
            return True
    for c in range(3):
        if all([marks[r][c] for r in range(3)]):
            return True
    if all([marks[rc][rc] for rc in range(3)]):
        return True
    if all([marks[rc][2 - rc] for rc in range(3)]):
        return True
    return False

def solve(A, B):
    marks = [[False] * 3 for _ in range(3)]    
    for b in B:
        for row in range(3):
            for col in range(3):
                if A[row][col] == b:
                    marks[row][col] = True
    return bingo(marks)

A = [[int(e) for e in input().split()] for _ in range(3)]
N = int(input())
B = [int(input()) for e in range(N)]

print("Yes" if solve(A, B) else "No")
