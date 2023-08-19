# B - Painting Balls with AtCoDeer

N, K = [int(e) for e in input().split()]

print(K if N == 1 else K * (K - 1) ** (N - 1))
