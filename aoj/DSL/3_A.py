# 3_A.py The Smallest Window I
# First try: AC 0.23s 16364KB
# Refactor: AD 0.15s 16360KB

N, S = [int(e) for e in input().split()]
A = [int(e) for e in input().split()]

start, end, min_length = 0, 0, float("inf")
sum = 0

for start in range(N):
    while sum < S and end < N:
        sum += A[end]
        end += 1
    if sum >= S:
        min_length = min(min_length, end - start)
    sum -= A[start]

print(min_length if min_length < float("inf") else 0)
