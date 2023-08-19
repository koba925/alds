# C - digitnum

MOD = 998244353

def sum_sequence(start, end):
    return ((start + end) * (end - start + 1) // 2) % MOD

def solve(N):
    ans = sum_sequence(1, min(N, 9))
    base = 10
    while base <= N:
        ans = (ans + sum_sequence(1, min(N - base + 1, 9 * base))) % MOD
        base *= 10
    return ans

N = int(input())
print(solve(N))
