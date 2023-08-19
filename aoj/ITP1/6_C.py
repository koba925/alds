# 6_C.py

n = int(input())

a = [[[0 for r in range(10)] for f in range(3)] for b in range(4)]

for i in range(n):
    b, f, r, v = map(int, input().split())
    a[b - 1][f - 1][r - 1] += v

for b in range(4):
    for f in range(3):
        for r in range(10):
            print(f" {a[b][f][r]}", end="")
        print()
    if (b != 3):
        print("####################")
