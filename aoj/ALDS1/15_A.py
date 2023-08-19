# 15_A.py Change Making

from typing import List

# recursion 0.06s 7156KB
# def changes(n: int, coins: List[int]) -> int:
#     if not coins:
#         return 0
#     c = n // coins[0]
#     return c + changes(n - c * coins[0], coins[1:])

# iterative 0.06s 7156KB
# def changes(n: int, coins: List[int]) -> int:
#     total = 0
#     for c in coins:
#         k = n // c
#         n -= c * k
#         total += k
#     return total

# divmod 0.06s 7156KB
def changes(n: int, coins: List[int]) -> int:
    total = 0
    for c in coins:
        k, n = divmod(n, c)
        total += k
    return total

n = int(input())
print(changes(n, [25, 10, 5, 1]))