def is_prime(N):
    if N < 2:
        return False
    n = 2
    while n * n <= N:
        if N % n == 0:
            return False
        n += 1
    return True


# 大きな数の素数判定ならMiller Rabinテストを用いる

import random


def miller_rabin(n):
    def test():
        a = random.randint(1, n - 1)
        if pow(a, t, n) == 1:
            return True

        for i in range(0, s):
            if pow(a, pow(2, i) * t, n) == n - 1:
                return True

        return False

    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    s, t = 0, n - 1
    while t % 2 == 0:
        s, t = s + 1, t // 2

    for i in range(20):
        if not test():
            return False
    return True


def primes_to(N):
    is_prime = [False, False] + [True] * (N - 1)
    n = 2
    while n * n <= N:
        if is_prime[n]:
            for m in range(2 * n, N + 1, n):
                is_prime[m] = False
        n += 1
    return [i for i, ip in enumerate(is_prime) if ip]


def primes_between(A, B):
    N = int((B + 1) ** 0.5)
    primes = primes_to(N)

    is_prime = [True] * (B - A + 1)

    for p in primes:
        min_multiple = (A + p - 1) // p * p
        if min_multiple == p:
            min_multiple *= 2
        for n in range(min_multiple, B + 1, p):
            is_prime[n - A] = False

    return [i for i, ip in enumerate(is_prime, A) if ip]


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


def number_of_divisors(N):
    factors = prime_factorize(N)
    return ()


def divisors_of(N):
    i, divisors = 1, []
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if N // i != i:
                divisors.append(N // i)
        i += 1
    return sorted(divisors)


A, B = [int(e) for e in input().split()]
print(len(primes_between(A, B)))
