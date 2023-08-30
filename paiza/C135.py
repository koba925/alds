import sys

M, D = [int(e) for e in sys.stdin.readline().split()]
P, N = [int(e) for e in sys.stdin.readline().split()]

discounted, normal = divmod(N, M)
print(int((M * discounted * P * (100 - D) // 100) + P * normal))
