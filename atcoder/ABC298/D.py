# D - Writing a Numeral

from sys import stdin
from functools import lru_cache

MOD = 998244353

@lru_cache
def pow10(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return pow10(n // 2) ** 2 % MOD
    else:
        return pow10(n - 1) * 10 % MOD

Q = int(stdin.readline())
S, left, right, ans = "1", 0, 0, 1
for line in stdin.readlines():
    command, *param = line.split()
    if command == "1":
        S += param[0]
        ans = (ans * 10 + int(param[0])) % MOD
        right += 1
    elif command == "2":
        ans = (ans - int(S[left]) * pow10(right - left)) % MOD
        left += 1
    elif command == "3":
        print(ans)
