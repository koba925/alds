# B - Quadruple

def solve(N, K):
    ans = 0
    for ab in range(2, 2 * N + 1):
        cd = ab - K
        if 2 <= cd <= 2 * N:
            ans += (min(ab, N + 1) - max(1, ab - N)) * (min(cd, N + 1) - max(1, cd - N))
    return ans

def solve_editorial(N, K):
    ans = 0
    for ab in range(2, 2 * N + 1):
        cd = ab - K
        if 2 <= cd <= 2 * N:
            ans += min(ab - 1, 2 * N + 1 - ab) * min(cd - 1, 2 * N + 1 - cd)
    return ans

N, K = [int(e) for e in input().split()]

print(solve_editorial(N, K))
