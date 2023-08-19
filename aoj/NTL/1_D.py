def prime_factorize(N):
    factors = []
    n = 2
    while n * n <= N:
        if N % n == 0:
            p = 0
            while N % n == 0:
                N //= n
                p += 1
            factors.append((n, p))
        n += 1
    if N != 1:
        factors.append((N, 1))
    return factors


def eulers_phy(n):
    for f, _ in prime_factorize(n):
        n -= n // f
    return n


n = int(input())
print(eulers_phy(n))
