def prime_factorize(N: int) -> list[tuple[int, int]]:
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


from itertools import repeat

n = int(input())

factors: list[int] = sum([list(repeat(f, p)) for f, p in prime_factorize(n)], [])

print(f"{n}: ", end="")
print(*factors)
