# 6_A.py Binary Search

# 01.78 s 16856 KB
def binary_search1(a, k):

    def rec(l, r):
        if r < l:
            return None
        m = (l + r) // 2
        if a[m] < k:
            return rec(m + 1, r)
        elif a[m] > k:
            return rec(l, m - 1)
        else:
            return m
    
    return rec(0, len(a) - 1)

# 02.11 s 16856 KB
def binary_search2(a, f):

    def rec(l, r):
        if l == r:
            return l
        m = (l + r) // 2
        return rec(l, m) if f(a[m]) else rec(m + 1, r)
    
    return rec(0, len(a))

def in_array2(a, k):
    l = binary_search2(a, lambda x: k <= x)
    print(l)
    return l < len(a) and a[l] == k

# 00.54 s 16876 KB
from bisect import bisect_left

def in_array3(a, k):
    l = bisect_left(a, k)
    return l < len(a) and a[l] == k

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
q = int(stdin.readline())
for _ in range(q):
    k = int(stdin.readline())
    print(1 if in_array2(a, k) else 0)
