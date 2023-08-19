# 1_B.py 0-1 Knapsack Problem

# exhaustive search: #14 TLE 
# def solve(n, weight, items):
#     def _solve(i, w):
#         if i == 0:
#             return 0
#         result = _solve(i - 1, w)
#         if items[i - 1][1] <= w:
#             result = max(result, _solve(i - 1, w - items[i - 1][1]) + items[i - 1][0])
#         return result
#     
#     return _solve(len(items), weight)

# memoize: 0.93s 24036KB
# def solve(n, weight, items):
#     memo = [[-1] * (weight + 1) for _ in range(n + 1)]
#
#     def _solve(i, w):
#         if memo[i][w] != -1:
#             return memo[i][w]
#         if i == 0:
#             result = 0
#         else:
#             result = _solve(i - 1, w)
#             if items[i - 1][1] <= w:
#                 result = max(result, _solve(i - 1, w - items[i - 1][1]) + items[i - 1][0])
#         memo[i][w] = result
#         return result
#
#     return _solve(len(items), weight)

# DP: 0.65s 25512KB
# def solve(n, weight, items):
#     dp = [[0] * (weight + 1) for _ in range(n + 1)]
#
#     for i in range(n):
#         for w in range(weight + 1):
#             result = dp[i][w]
#             if items[i][1] <= w:
#                 result = max(result, dp[i][w - items[i][1]] + items[i][0])
#             dp[i + 1][w] = result
#
#     return dp[n][weight]

# 1-d DP: 0.42s 5928KB
def solve(n, weight, items):
    dp = [0] * (weight + 1)

    for i in range(n):
        for w in reversed(range(items[i][1], weight + 1)):
            dp[w] = max(dp[w], dp[w - items[i][1]] + items[i][0])

    return dp[weight]

from sys import stdin

# print(solve(4, 5, [[4, 2], [5, 2], [2, 1], [8, 3]]))
# exit()

n, w = [int(e) for e in stdin.readline().split()]
items = [[int(e) for e in line.split()] for line in stdin.readlines()]
print(solve(n, w, items))
