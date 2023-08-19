# 6_B.py

def partition(A, p, r):
    x = A[r]
    i = p
    for j in range(p, r):
        if A[j] <= x:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i], A[r] = A[r], A[i]
    return i


n = int(input())
A = [int(e) for e in input().split()]

q = partition(A, 0, n - 1)

print(*[f"[{e}]" if i == q else e for i, e in enumerate(A)])

