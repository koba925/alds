# 11_C.py Enumeration of Subsets III

from typing import List, Generator

def elements(n: int, subset: int) -> List[int]:
    ret = []
    for i in range(n):
        if subset & 1 == 1:
            ret.append(i)
        subset >>= 1
    return ret

def to_int(s: List[int]) -> int:
    return sum([2 ** i for i in s])

# enumerate by bit operation 02.59 s 18092 KB
# See プログラミングコンテストチャレンジブック第2版 p.144

def subsets(T: int) -> List[int]:
    ret = []
    S = T
    while True:
        ret.append(S)
        if S == 0:
            break
        S = (S - 1) & T
    return ret

n = int(input())
T = sum([2 ** int(e) for e in input().split()][1:])

for s in reversed(subsets(T)):
    print(f"{s}:", *elements(n, s))

# list + recuresive 02.94 s 7848 KB

# def enumerate(t: List[int]) -> Generator[List[int], None, None]:
    
#     def enum(t: List[int], s: List[int]) -> Generator[List[int], None, None]:
#         if not t:
#             yield s
#         else: 
#             yield from enum(t[:-1], s)           
#             yield from enum(t[:-1], [t[-1]] + s)           

#     yield from enum(t, [])

# n = int(input())
# t = [int(e) for e in input().split()][1:]
# for s in enumerate(t):
#     print(f"{to_int(s)}:", *s)

# combinations 03.60 s 20660 KB

# from itertools import combinations

# n = int(input())
# t = [int(e) for e in input().split()][1:]
# ans = []
# for l in range(len(t) + 1):
#     for s in combinations(t, l):
#         ans.append(to_int(list(s)))
# for ss in sorted(ans):
#     print(f"{ss}:", *elements(n, ss))