# 6_B.py Includes

from sys import stdin

# 00.15 s 55864 KB

# n = int(stdin.readline())
# a = {int(e) for e in stdin.readline().split()}
# m = int(stdin.readline())
# b = {int(e) for e in stdin.readline().split()}

# print(1 if a.issuperset(b) else 0)

# 00.28 s 36512 KB
# def includes(a, b):
#     ai, alen, bi, blen = 0, len(a), 0, len(b)
#     while ai < alen and bi < blen:
#         if a[ai] == b[bi]:
#             bi += 1
#         elif a[ai] < b[bi]:
#             ai += 1
#         elif a[ai] > b[bi]:
#             return False
#     return bi == len(b)

# 同じ数字が続かないと仮定
# 00.23 s 36508 KB
def includes(a, b):
    ai, alen, bi, blen = 0, len(a), 0, len(b)
    while ai < alen and bi < blen:
        if a[ai] == b[bi]:
            bi += 1
        elif a[ai] > b[bi]:
            return False
        ai += 1
    return bi == len(b)

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
m = int(stdin.readline())
b = [int(e) for e in stdin.readline().split()]

print(1 if includes(a, b) else 0)
