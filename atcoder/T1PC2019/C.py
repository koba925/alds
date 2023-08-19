# C - Stones

def solve(N, S):
    count = [1 if ch == "#" else 0 for ch in S]
    for i in range(1, N):
        count[i] += count[i - 1]

    min_change = N - count[N - 1]
    for i in range(N):
        left = count[i]
        right = N - 1 - i - (count[N - 1] - count[i])
        min_change = min(min_change, left + right)

    return min_change
        
N = int(input())
S = input()

print(solve(N, S))
