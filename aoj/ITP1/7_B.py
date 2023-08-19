# 7_B.py

def solve(n, x):
    count = 0
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            k = x - i - j
            if j < k <= n:
                # print(i, j, k)
                count += 1
    return count

while True:
    n, x = [int(e) for e in input().split()]
    if n == 0 and x == 0:
        break
    print(solve(n, x))
