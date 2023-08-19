# 3_B.py The Smallest Window II

N, K = [int(e) for e in input().split()]
A = [int(e) for e in input().split()]

start, end, min_length = 0, 0, float("inf")

# First Implementation: #35 4.99s TLE #34 1.09s #31 0.39s
# counts = [0] * K
# for start in range(N):
#     while not all([e > 0 for e in counts]):
#         if end == N:
#             break
#         if A[end] <= K:
#             counts[A[end] - 1] += 1
#         end += 1
#     else:
#         min_length = min(min_length, end - start)
#     if A[start] <= K:
#         counts[A[start] - 1] -= 1

# Record complete counts: AC 0.22s
counts = [0] * K
comp = 0
for start in range(N):
    while comp < K and end < N:
        if A[end] <= K:
            if counts[A[end] - 1] == 0:
                comp += 1
            counts[A[end] - 1] += 1
        end += 1
    if comp == K:
        min_length = min(min_length, end - start)
    if A[start] <= K:
        counts[A[start] - 1] -= 1
        if counts[A[start] - 1] == 0:
            comp -= 1

print(min_length if min_length < float("inf") else 0)
