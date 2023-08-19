# B - Minesweeper

def solve(H, W, S):
    neighbors = [(-1, -1), (-1, 0), (-1, 1), 
                 ( 0, -1),          ( 0, 1), 
                 ( 1, -1), ( 1, 0), ( 1, 1)]

    def bombs(r, c):
        b = 0
        for dr, dc in neighbors:
            row, col = r + dr, c + dc
            if 0 <= row < H and 0 <= col < W and S[row][col] == "#":
                b += 1
        return b
    
    for r in range(H):
        for c in range(W):
            print("#" if S[r][c] == "#" else bombs(r, c), end="")
        print()

H, W = [int(e) for e in input().split()]
S = [input() for _ in range(H)]
solve(H, W, S)
