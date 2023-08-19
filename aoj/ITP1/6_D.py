# 6_D.py

n, m = map(int, input().split())

a = [list(map(int, input().split())) for i in range(n)]
b = [int(input()) for i in range(m)]
c = [sum([ai[j] * b[j] for j in range(m)]) for ai in a]
print(*c, sep="\n")
