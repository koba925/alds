# D - Divide by 2 or 3

def factor23(n):
    f2 = 0
    while n % 2 == 0:
        f2 += 1
        n //= 2
    f3 = 0
    while n % 3 == 0:
        f3 += 1
        n //= 3
    return f2, f3, n

def solve_mine(N, A):
    factors = [factor23(a) for a in A]
    if not all(rest == factors[0][2] for _, _, rest in factors):
        return -1
    sum2 = sum([f2 for f2, _, _ in factors])
    sum3 = sum([f3 for _, f3, _ in factors])
    min2 = min([f2 for f2, _, _ in factors])
    min3 = min([f3 for _, f3, _ in factors])
    return sum2 + sum3 - min2 * N - min3 * N

from math import gcd

def solve_editorial(N, A):
    g = 0
    for a in A:
        g = gcd(g, a)
    
    B = [a // g for a in A]
    factors = [factor23(a) for a in B]
    if any(rest != 1 for _, _, rest in factors):
        return -1
    sum2 = sum([f2 for f2, _, _ in factors])
    sum3 = sum([f3 for _, f3, _ in factors])
    return sum2 + sum3

N = int(input())
A = [int(e) for e in input().split()]
print(solve_editorial(N, A))
