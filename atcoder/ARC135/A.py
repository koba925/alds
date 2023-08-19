# A - Floor, Ceil - Decomposition

from functools import lru_cache

@lru_cache
def solve(X):
    return X if X <= 4 else solve(X // 2) * solve((X + 1) // 2) % 998244353

# print(solve(3)) # 3
# print(solve(15)) # 192
# print(solve(100)) # 824552442

X = int(input())
print(solve(X))
