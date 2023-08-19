# C - Attention

N = int(input())
S = input()

# First Solution
# min_turn = turn = len([c for c in S[1:] if c == "E"])
# for i in range(1, N):
#     if S[i - 1] == "W": 
#         turn += 1
#     if S[i] == "E":
#         turn -= 1
#     min_turn = min(min_turn, turn)

# Cumulative Sum
E, W = [0] * N, [0] * N

for i in range(N):
    if S[i] == "E":
        E[i] = 1
    else:
        W[i] = 1

for i in range(1, N):
    E[i] += E[i - 1]
    W[i] += W[i - 1]

min_turn = E[N - 1] - E[0]
for i in range(1, N - 1):
    min_turn = min(min_turn, W[i - 1] + (E[N - 1] - E[i]))
min_turn = min(min_turn, W[N - 1])

print(min_turn)
