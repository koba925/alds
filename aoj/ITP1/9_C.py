# 9_C.py

n = int(input())
t = 0
h = 0

for i in range(n):
    tc, hc = input().split()
    if tc > hc:
        t += 3
    elif tc < hc:
        h += 3
    else:
        t += 1
        h += 1

print(t, h)
