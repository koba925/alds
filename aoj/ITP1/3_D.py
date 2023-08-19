# 3_D.py

a, b, c = [int(e) for e in input().split()]

n = 0
for i in range(a, b + 1):
    if c % i == 0:
        n += 1

print(n)