# 11_A.py Enumeration of Subsets I

from typing import List

n = int(input())

def elements(n: int, subset: int) -> List[int]:
    ret = []
    for i in range(n):
        if subset & 1 == 1:
            ret.append(i)
        subset >>= 1
    return ret

for i in range(2 ** n):
    print(f"{i}:", *elements(n, i))
