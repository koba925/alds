# TK: Range Minimum Query (RMQ)
# TK: セグメント木 Segment Tree


#######################################################################
# using ac-library-python https://github.com/not522/ac-library-python/
# does not run on AOJ
#######################################################################

from atcoder.segtree import SegTree

MAXVAL = 2**31 - 1

n, q = [int(e) for e in input().split()]

A = SegTree(min, MAXVAL, n)

for _ in range(q):
    com, x, y = [int(e) for e in input().split()]
    match com:
        case 0: A.set(x, y)
        case 1: print(A.prod(x, y + 1))

exit()

#######################################################################
# my code in the past
#######################################################################

MAXVAL = 2**31 - 1

# naive: #12 TLE
# class Items:
#     def __init__(self, n) -> None:
#         self.items = [MAXVAL] * n
#     def update(self, i, x):
#         self.items[i] = x
#     def find(self, s, t):
#         return min(self.items[s:t+1])

# dict: #12 TLE
# class Items:
#     def __init__(self, n) -> None:
#         self.items = {}
#     def update(self, i, x):
#         self.items[i] = x
#     def find(self, s, t):
#         vals = [v for k, v in self.items.items() if s <= k <= t]
#         return min(vals) if vals else MAXVAL

# dict + binary search:  #12 TLE
# from bisect import bisect_left, bisect_right
# class Items:
#     def __init__(self, n) -> None:
#         self.items = {}
#     def update(self, i, x):
#         self.items[i] = x
#     def find(self, s, t):
#         allpairs = sorted([(k, v) for k, v in self.items.items()])
#         left = bisect_left(allpairs, (s, 0))
#         right = bisect_left(allpairs, (t + 1, 0))
#         vals = [v for _, v in allpairs[left:right]]
#         return min(vals) if vals else MAXVAL

# list + binary searcy:  #12 TLE
# from bisect import bisect_left, bisect_right
# class Items:
#     def __init__(self, n) -> None:
#         self.keys = []
#         self.vals = []
#     def update(self, i, x):
#         k = bisect_left(self.keys, i)
#         if k < len(self.keys) and self.keys[k] == i:
#             self.vals[k] = x
#         else:
#             self.keys[k:k] = [i]
#             self.vals[k:k] = [x]
#     def find(self, s, t):
#         left = bisect_left(self.keys, s)
#         right = bisect_right(self.keys, t)
#         vals = self.vals[left:right]
#         return min(vals) if vals else MAXVAL

# range minimum query: AC 3.20s
class RangeMinimumQuery:
    def __init__(self, size) -> None:
        def actual_size(size):
            asize = 1
            while asize < size:
                asize *= 2
            return asize

        self.size = size
        self.asize = actual_size(size)
        self.vals = [MAXVAL] * (self.asize * 2 - 1)

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return i * 2 + 1

    def right_child(self, i):
        return i * 2 + 2

    def update(self, i, x):
        i += self.asize - 1
        self.vals[i] = x
        while i > 0:
            i = self.parent(i)
            self.vals[i] = min(self.vals[self.left_child(i)],
                               self.vals[self.right_child(i)])

    # find the minimum value from [s, t)
    def find(self, s, t):
        def _find(s, t, i, l, r):
            if r <= s or t <= l:
                return MAXVAL
            if s <= l and r <= t:
                return self.vals[i]
            vl = _find(s, t, self.left_child(i), l, (l + r) // 2)
            vr = _find(s, t, self.right_child(i), (l + r) // 2, r)
            return min(vl, vr)

        return _find(s, t, 0, 0, self.asize)

from sys import stdin

n, q = [int(e) for e in stdin.readline().split()]
#a = Items(n)
a = RangeMinimumQuery(n)

for line in stdin.readlines():
    com, *param = [int(e) for e in line.split()]
    if com == 0:
        a.update(param[0], param[1])
    elif com == 1:
        print(a.find(param[0], param[1] + 1))
