# 6_C.py

from sys import stdin
from math import inf


def is_stable(a, b):
    for ai in a:
        for bj in b:
            if ai[1] == bj[1]:
                if ai[0] == bj[0]:
                    b.remove(bj)
                    break
                else:
                    return False
    return True

def quicksort(a, f=lambda x: x):
    def partition(p, r):
        x = a[r]
        i = p
        for j in range(p, r):
            if f(a[j]) <= f(x):
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[r] = a[r], a[i]
        return i

    def rec(p, r):
        if p < r:
            q = partition(p, r)
            rec(p, q - 1)
            rec(q + 1, r)

    rec(0, len(a) - 1)


n = int(stdin.readline())
A = [(suit, int(num)) for suit, num
     in [line.split() for line in stdin.readlines()]]
B = A[:]

quicksort(A, lambda x: x[1])
print("Stable" if is_stable(A, B) else "Not stable")
print(*[f"{suit} {num}" for suit, num in A], sep="\n")
