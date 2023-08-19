# 1_D.py Longest Increasing Subsequence 最長増加部分列

from sys import stdin

# O(n^2) DP: TLE
def solve(n, a):
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if a[j] < a[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# use bisect: 0.13s 16868KB
from bisect import bisect_left
def solve(n, a):
    lis = [a[0]]
    for ai in a[1:]:
        if lis[-1] < ai:
            lis.append(ai)
        else:
            lis[bisect_left(lis, ai)] = ai
    return len(lis)

print(solve(5, [5, 1, 3, 2, 4]))
print(solve(3, [1, 1, 1]))
exit()

n = int(stdin.readline())
a = [int(e) for e in stdin.readlines()]
print(solve(n, a))
