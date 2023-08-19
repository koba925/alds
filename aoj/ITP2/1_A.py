# 1_A.py

A = []

q = int(input())
for _ in range(q):
    query = [int(e) for e in input().split()]
    if query[0] == 0:
        A.append(query[1])
    elif query[0] == 1:
        print(A[query[1]])
    else:
        A.pop()
