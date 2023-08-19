# 1_C.py

def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 大きな数の素数判定ならMiller Rabinテストを用いる

import random

def miller_rabin(n):
    def test():
        a = random.randint(1, n - 1)
        if pow(a, t, n) == 1: return True

        for i in range(0, s):
            if pow(a, pow(2, i) * t, n) == n - 1:
                return True

        return False

    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False

    s, t = 0, n - 1
    while t % 2 == 0:
        s, t = s + 1, t // 2

    for i in range(20):
        if not test(): return False
    return True

n = int(input())

c = 0
for i in range(n):
    if miller_rabin(int(input())):
        c += 1

print(c)