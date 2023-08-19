# 1_D.py

n = int(input())

# 00.55 s 13596 KB
# R = [int(input()) for _ in range(n)]

# 00.59 s 5612 KB
R_min = int(input())

max_profit = -10**9

for t in range(1, n):
    R = int(input())
    max_profit = max(max_profit, R - R_min)
    R_min = min(R_min, R)

print(max_profit)
