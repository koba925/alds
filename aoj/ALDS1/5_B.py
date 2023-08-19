# 5_B.py

import math

def mergesort(A):

    compare = 0

    def merge(left, mid, right):
        nonlocal compare

        L = A[left:mid] + [math.inf]
        R = A[mid:right] + [math.inf]
        i, j = 0, 0
        for k in range(left, right):
            compare += 1
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def rec(left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            rec(left, mid)
            rec(mid, right)
            merge(left, mid, right)

    rec(0, len(A))
    return compare

n = int(input())
S = [int(e) for e in input().split()]
compare = mergesort(S)
print(*S)
print(compare)

