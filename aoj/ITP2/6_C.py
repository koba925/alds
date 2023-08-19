# 6_C.py Lower Bound

# standard library 00.42 s 24824 KB
# from bisect import bisect_left

# iterative 01.03 s 24808 KB
# def bisect_left(a, k):
#     l, r = 0, len(a)
#     while l < r:
#         m = (l + r) // 2
#         if a[m] < k:
#             l = m + 1
#         else:
#             r = m
#     return l

# recursive 01.60 s 24920 KB
def bisect_left(a, k):

    def rec(l, r):
        if l == r:
            return l
        m = (l + r) // 2
        return rec(m + 1, r) if a[m] < k else rec(l, m)

    return rec(0, len(a))

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for k in stdin.readlines():
    print(bisect_left(a, int(k)))
