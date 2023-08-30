import sys

N, M = [int(e) for e in sys.stdin.readline().split()]
A = [int(sys.stdin.readline()) for _ in range(N)]
B = [int(sys.stdin.readline()) for _ in range(M)]

C = [0] * N

gi = 0
for b in B:
    while b > 0:
        n = min(b, A[gi])
        C[gi] += n
        b -= n
        gi = (gi + 1) % N

print(*C, sep="\n")
