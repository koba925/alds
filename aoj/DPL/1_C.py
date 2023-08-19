# 1_C.py Knapsack Problem

# exhaustive search: #8 TLE
def solve(n, weight, items):
    def _solve(i, w):
        if i == 0:
            return 0
        result = _solve(i - 1, w)
        if items[i - 1][1] <= w:
            result = max(result, _solve(i, w - items[i - 1][1]) + items[i - 1][0])
        return result

    return _solve(len(items), weight)

# memoize: 1.43s 28020KB
def solve(n, weight, items):
    memo = [[-1] * (weight + 1) for _ in range(len(items) + 1)]

    def _solve(i, w):
        if memo[i][w] != -1:
            return memo[i][w]
        if i == 0:
            result = 0
        else:
            result = _solve(i - 1, w)
            if items[i - 1][1] <= w:
                result = max(result, _solve(i, w - items[i - 1][1]) + items[i - 1][0])
        memo[i][w] = result
        return result

    return _solve(len(items), weight)

# DP: 0.70s 15716KB
def solve(n, weight, items):
    dp = [[0] * (weight + 1) for _ in range(len(items) + 1)]

    for i in range(1, n + 1):
        for w in range(weight + 1):
            result = dp[i - 1][w]
            if items[i - 1][1] <= w:
                result = max(result, dp[i][w - items[i - 1][1]] + items[i - 1][0])
            dp[i][w] = result

    return dp[len(items)][weight]

# 1-d DP: 0.49s 5940KB
def solve(n, weight, items):
    dp = [0] * (weight + 1)

    for i in range(1, n + 1):
        for w in range(items[i - 1][1], weight + 1):
            dp[w] = max(dp[w], dp[w - items[i - 1][1]] + items[i - 1][0])

    return dp[weight]

from sys import stdin, setrecursionlimit
setrecursionlimit(20000)

print(solve(4, 8, [[4, 2], [5, 2], [2, 1], [8, 3]]))
print(solve(2, 20, [[5, 9],[4, 10]]))
exit()

n, w = [int(e) for e in stdin.readline().split()]
items = [[int(e) for e in line.split()] for line in stdin.readlines()]
print(solve(n, w, items))
