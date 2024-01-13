H, W = [int(e) for e in input().split()]
A = [[int(e) for e in input().split()] for _ in range(H)]

characters = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for row in range(H):
  print("".join(characters[a] for a in A[row]))
