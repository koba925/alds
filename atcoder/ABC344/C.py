N = int(input())
A = [int(e) for e in input().split()]
M = int(input())
B = [int(e) for e in input().split()]
L = int(input())
C = [int(e) for e in input().split()]
Q = int(input())
X = [int(e) for e in input().split()]

S = set()
for a in A:
    for b in B:
        for c in C:
            S.add(a + b + c)

for x in X:
    print("Yes" if x in S else "No")