# 1_A.py Coin Changing Problem

from sys import setrecursionlimit
setrecursionlimit(100000)

# exhaustive search #9 TLE
# def changes(total, coins):
#     def _changes(i, rest):
#         if i == 0:
#             return rest
#         result = _changes(i - 1, rest)
#         if rest >= coins[i]:
#             result = min(result, 1 + _changes(i, rest - coins[i]))
#         return result
#     return _changes(len(coins) - 1, total)

# memoize: AC 1.08s 69316KB
# def changes(total, coins):
#     memo = [[-1] * (total + 1) for _ in range(len(coins))]
#
#     def _changes(i, rest):
#         if memo[i][rest] != -1:
#             return memo[i][rest]
#         if i == 0:
#             result = rest
#         else:
#             result = _changes(i - 1, rest)
#             if rest >= coins[i]:
#                 result = min(result, 1 + _changes(i, rest - coins[i]))
#         memo[i][rest] = result
#         return result
#   
#     return _changes(len(coins) - 1, total)

# DP: 0.56s 43252KB
# def changes(total, coins):
#     dp = [[float("inf")] * (total + 1) for _ in range(len(coins))]

#     for rest in range(total + 1):
#         dp[0][rest] = rest

#     for i in range(1, len(coins)):
#         for rest in range(total + 1):
#             result = dp[i - 1][rest]
#             if rest >= coins[i]:
#                 result = min(result, 1 + dp[i][rest - coins[i]])
#             dp[i][rest] = result
#     return dp[len(coins) - 1][total]

# 1-D DP: 0.36s 7520KB
def changes(total, coins):
    dp = list(range(total + 1))
    for i in range(1, len(coins)):
        for rest in range(coins[i], total + 1):
            dp[rest] = min(dp[rest], 1 + dp[rest - coins[i]])
    return dp[total]

def solve(n, m, coins):
    print(changes(n, coins))
        
# solve(8, 3, [1, 4, 5])
# solve(65, 6, [1, 2, 7, 8, 12, 50])
# exit()

n, m = [int(e) for e in input().split()]
coins = [int(e) for e in input().split()]

solve(n, m, coins)
