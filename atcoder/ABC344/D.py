T = input()
N = int(input())

A = []
S = []
for _ in range(N):
    a, *s = input().split()
    A.append(int(a))
    S.append(s)

MAX = 101
pmemo = [0] + [MAX] * len(T)
for i in range(N):
    memo = pmemo[:]
    ss = S[i]
    for j in range(A[i]):
        s = ss[j]
        for k in range(1, len(T) + 1):
            if k >= len(s) and pmemo[k - len(s)] != MAX and T[k - len(s):k] == s:
                memo[k] = min(memo[k], pmemo[k - len(s)] + 1)
    pmemo = memo

print(-1 if memo[-1] == MAX else memo[-1])


"""
a
1
1 a

1

aa
2
2 b a
2 c a

2

aa
2
2 b a
3 c a aa

"""