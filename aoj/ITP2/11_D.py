# 11_D.py Enumeration of Combinations

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

n, k = [int(e) for e in input().split()]

# By bitwise operation 00.48 s 7824 KB
# See プログラミングコンテストチャレンジブック第2版 p.144
t: int = (1 << k) - 1
while t < (1 << n):
    print(f"{t}:", *elements(n, t))
    # print(f"t                    = {t:0{n}b}")
    # print(f"-t                   = {-t & (2**n - 1):0{n}b}")
    x = t & -t
    # print(f"x                    = {x:0{n}b}")
    y = t + x
    # print(f"y                    = {y:0{n}b}")
    # print(f"t & ~y               = {t & ~y:0{n}b}")
    # print(f"t & ~y // x          = {t & ~y // x:0{n}b}")
    # print(f"((t & ~y) // x) >> 1 = {((t & ~y) // x) >> 1:0{n}b}")
    t = (((t & ~y) // x) >> 1) | y
    # print("---")

# from itertools import combinations

# 00.47 s 19124 KB
# ans = [(to_int(list(sst)), sst) for sst in combinations(range(n), k)]
# for ssi, sst in sorted(ans):
#     print(f"{ssi}:", *sst)

# 00.61 s 10140 KB
# ans = [to_int(list(sst)) for sst in combinations(range(n), k)]
# for ssi in sorted(ans):
#     print(f"{ssi}:", *elements(n, ssi))
