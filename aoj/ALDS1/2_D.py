# 2-D.py

import sys

def shell_sort(a, g):
    def insertion_sort(a, gi):
        cnt = 0
        for i in range(gi, n):
            v = a[i]
            j = i - gi
            while j >= 0 and a[j] > v:
                a[j + gi] = a[j]
                j -= gi
                cnt += 1
            a[j + gi] = v
        return cnt

    cnt = 0
    for gi in g:
        cnt += insertion_sort(a, gi)

    return cnt

n = int(input())
a = [int(e) for e in sys.stdin.readlines()]
g = [e for e in [797161, 265720, 88573, 29524, 9841, 3280, 1093, 364, 121, 40, 13, 4, 1] if e <= n]

print(len(g))
print(*g)
print(shell_sort(a, g))
print(*a, sep="\n")
