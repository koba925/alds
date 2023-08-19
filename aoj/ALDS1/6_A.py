# 6_A.py

def counting_sort(A, maxA):
    B = [0] * len(A)
    C = [0] * (maxA + 1)
    
    for a in A:
        C[a] += 1

    for i in range(len(C) - 1):
        C[i + 1] += C[i]

    for  i in range(len(A)):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return B

n = int(input())
A = [int(e) for e in input().split()]

print(*counting_sort(A, 10000))
