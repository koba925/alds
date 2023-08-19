# 11_B.py Enumeration of Subsets II

from typing import List

def elements(n: int, subset: int) -> List[int]:
    ret = []
    for i in range(n):
        if subset & 1 == 1:
            ret.append(i)
        subset >>= 1
    return ret

n = int(input())
T = 0
for i in [int(e) for e in input().split()][1:]:
    T += 2 ** i

for i in range(2 ** n):
    if i | T == i:
        print(f"{i}:", *elements(n, i))
