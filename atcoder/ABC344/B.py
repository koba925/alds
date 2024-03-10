A = []
while True:
    a = int(input())
    A.append(a)
    if a == 0: break
print(*reversed(A), sep="\n")
