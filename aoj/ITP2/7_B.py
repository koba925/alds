# 7_B.py Set: Delete
# TODO: Better Data Structure?

from sys import stdin
from typing import List

from bisect import bisect_left, bisect_right

# use sorted list
# #15 3.79s but TLE

def insert(s: List[int], x: int) -> None:
    p = bisect_left(s, x)
    if p == len(s) or s[p] != x:
        s.insert(p, x)

def find(s: List[int], x: int) -> int:
    p = bisect_left(s, x)
    return 1 if p < len(s) and s[p] == x else 0

def delete(s: List[int], x: int) -> None:
    p = bisect_left(s, x)
    if p < len(s) and s[p] == x:
        del s[p]

def dump(s: List[int], l: int, r: int) -> None:
    lp = bisect_left(s, l)
    rp = bisect_right(s, r)
    for i in range(lp, rp):
        print(s[i])

q = int(stdin.readline())
s: List[int] = []

for query in stdin.readlines():
    command, *param = [int(e) for e in query.split()]
    if command == 0:
        insert(s, param[0])
        print(len(s))
    elif command == 1:
        print(find(s, param[0]))
    elif command == 2:
        delete(s, param[0])
    else:
        dump(s, param[0], param[1])

# use builtin set TLE

# q = int(stdin.readline())
# s = set()
# for query in stdin.readlines():
#     command, *param = [int(e) for e in query.split()]
#     if command == 0:
#         s.add(param[0])
#         print(len(s))
#     elif command == 1:
#         print(1 if param[0] in s else 0)
#     elif command == 2:
#         s.discard(param[0])
#     else:
#         # #15 0.86s
#         ss = sorted(s)
#         l = bisect_left(ss, param[0])
#         r = bisect_right(ss, param[1])
#         if l < r: print("\n".join([str(e) for e in ss[l:r]]))

#         # #15 1.17s
#         # result = sorted([e for e in s if param[0] <= e <= param[1]])
#         # if result:
#         #     print("\n".join([str(e) for e in result]))

#         # #15 1.21s
#         # result = sorted([e for e in s if param[0] <= e <= param[1]])
#         # if result:
#         #     print(*result, sep="\n")

#         # #15 1.43s
#         # for e in sorted([e for e in s if param[0] <= e <= param[1]]):
#         #     print(e)

