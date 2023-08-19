# 6_D.py Equal Range

# standard library 00.64 s 24828 KB
# from bisect import bisect_left, bisect_right

from typing import List

# iterative 01.87 s 24804 KB
# def bisect_left(a, k):
#     l, r = 0, len(a)
#     while l < r:
#         m = (l + r) // 2
#         if a[m] < k:
#             l = m + 1
#         else:
#             r = m
#     return l

# def bisect_right(a, k):
#     l, r = 0, len(a)
#     while l < r:
#         m = (l + r) // 2
#         if a[m] <= k:
#             l = m + 1
#         else:
#             r = m
#     return l

# recursive 02.87 s 24924 KB
# with type hints 03.10 s 26576 KB
def bisect_left(a: List[int], k: int) -> int:

    def rec(l: int, r: int) -> int:
        if l == r:
            return l
        m = (l + r) // 2
        return rec(m + 1, r) if a[m] < k else rec(l, m)

    return rec(0, len(a))

def bisect_right(a: List[int], k: int) -> int:

    def rec(l: int, r: int) -> int:
        if l == r:
            return l
        m = (l + r) // 2
        return rec(m + 1, r) if a[m] <= k else rec(l, m)

    return rec(0, len(a))

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())

for k in stdin.readlines():
    print(bisect_left(a, int(k)), bisect_right(a, int(k)))
