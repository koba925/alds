# 7_D.py Multi-set

from sys import stdin
from typing import List

from bisect import bisect_left, bisect_right, insort_left

# use sorted list

def insert(s: List[int], x: int) -> None:
    insort_left(s, x)

def find(s: List[int], x: int) -> int:
    lp = bisect_left(s, x)
    rp = bisect_right(s, x)
    return rp -lp

def delete(s: List[int], x: int) -> None:
    lp = bisect_left(s, x)
    rp = bisect_right(s, x)
    s[lp:rp] = []

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
