# 5_D.py

from math import inf

def number_of_inverse(a):
    def merge(left, mid, right):
        nonlocal inverse

        L = a[left:mid] + [inf]
        R = a[mid:right] + [inf]
        i, j = 0, 0
        for k in range(left, right):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                inverse += mid + j - k
                a[k] = R[j]
                j += 1

    def rec(left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            rec(left, mid)
            rec(mid, right)
            merge(left, mid, right)

    inverse = 0
    rec(0, len(a))
    return inverse

n = int(input())
a = [int(e) for e in input().split()]
print(number_of_inverse(a))
