# 3_D.py Sliding Minimum Element

# defaultdict: #23 1.13s #24 TLE
# from collections import defaultdict
#
# def solve(n, l, a):
#     def add(ai):
#         counter[ai] += 1
#
#     def delete(ai):
#         count = counter[ai] - 1
#         if count == 0:
#             del counter[ai]
#         else:
#             counter[ai] = count
#
#     ret = []
#     counter = defaultdict(int)
#     for ai in a[:l]:
#         add(ai)
#     ret.append(min(counter.keys()))
#     for i in range(n - l):
#         delete(a[i])
#         add(a[i + l])
#         ret.append(min(counter.keys()))
#     return ret

# RMQ: #23 4.65s #24 TLE
# 
# MAXVAL = 10 ** 10
# 
# class RangeMinimumQuery:
#     def __init__(self, size) -> None:
#         def actual_size(size):
#             asize = 1
#             while asize < size:
#                 asize *= 2
#             return asize
# 
#         self.size = size
#         self.asize = actual_size(size)
#         self.vals = [MAXVAL] * (self.asize * 2 - 1)
# 
#     def parent(self, i):
#         return (i - 1) // 2
# 
#     def left_child(self, i):
#         return i * 2 + 1
# 
#     def right_child(self, i):
#         return i * 2 + 2
# 
#     def update(self, i, x):
#         i += self.asize - 1
#         self.vals[i] = x
#         while i > 0:
#             i = self.parent(i)
#             self.vals[i] = min(self.vals[self.left_child(i)],
#                                self.vals[self.right_child(i)])
# 
#     # find the minimum value from [s, t)
#     def find(self, s, t):
#         def _find(s, t, i, l, r):
#             if r <= s or t <= l:
#                 return MAXVAL
#             if s <= l and r <= t:
#                 return self.vals[i]
#             vl = _find(s, t, self.left_child(i), l, (l + r) // 2)
#             vr = _find(s, t, self.right_child(i), (l + r) // 2, r)
#             return min(vl, vr)
# 
#         return _find(s, t, 0, 0, self.asize)
# 
# def solve(n, l, a):
# 
#     ret = []
#     rmq = RangeMinimumQuery(n)
#     for i, ai in enumerate(a):
#         rmq.update(i, ai)
#     for i in range(n - l + 1):
#         ret.append(rmq.find(i, i + l))
#     return ret

# sliding: AC 1.45s 126252KB
from collections import deque

def solve(n, l, a):
    ret = []
    dq = deque()
    for i, ai in enumerate(a):
        while dq and ai <= dq[-1][1]:
            dq.pop()
        dq.append((i, ai))
        ret.append(dq[0][1])
        if dq[0][0] == i + 1 - l:
            dq.popleft()
    return ret[l - 1:]

n, l = [int(e) for e in input().split()]
a = [int(e) for e in input().split()]

print(*solve(n, l, a))
