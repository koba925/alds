# 5-A.py

MAX = 2000

def make_table(A):
    def rec(k, s):
        if s > MAX:
            return
        T[s] = True
        
        if k >= len(A):
            return
        rec(k + 1, s)
        rec(k + 1, s + A[k])

    T = [False] * (MAX + 1)
    rec(0, 0)
    return T

n = int(input())
A = [int(e) for e in input().split()]
q = int(input())
M = [int(e) for e in input().split()]

T = make_table(A)

for m in M:
    print("yes" if T[m] else "no")
