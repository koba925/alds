# 14_C.py Pattern Search
# TODO: use more sophisticated algorithm

from sys import stdin
from typing import List

# naive 4-nested loop -> TLE #12 9.45s #13 4.52s
# def solve(H: int, W: int, F: List[List[str]], R: int, C: int, P:List[List[str]]) -> None:

#     def match(h: int, w: int) -> bool:
#         for r in range(R):
#             for c in range(C):
#                 if F[h + r][w + c] != P[r][c]:
#                     return False
#         return True

#     for h in range(H - R + 1):
#         for w in range(W - C + 1):
#             if match(h, w):
#                 print(h, w)

# H, W = [int(e) for e in stdin.readline().split()]
# F = [list(stdin.readline().strip()) for _ in range(H)]
# R, C = [int(e) for e in stdin.readline().split()]
# P = [list(stdin.readline().strip()) for _ in range(H)]


# use string -> #21 TLE #12 1.83s #13 0.95s -> slower!!
# def solve(H: int, W: int, F: List[str], R: int, C: int, P:List[str]) -> None:

#     def match(h: int, w: int) -> bool:
#         for r in range(0, R):
#             if F[h + r][w:w + C] != P[r]:
#                 return False
#         return True

#     for h in range(H - R + 1):
#         for w in range(W - C + 1):
#             if match(h, w):
#                 print(h, w)

# use find -> #21 TLE #12 1.96s #13 1.00s -> slower!!
# def solve(H: int, W: int, F: List[str], R: int, C: int, P:List[str]) -> None:

#     def match(h: int, w: int) -> bool:
#         for r in range(1, R):
#             if F[h + r][w:w + C] != P[r]:
#                 return False
#         return True

#     for h in range(H - R + 1):
#         w = -1
#         while w <= W - C:
#             w = F[h].find(P[0], w + 1)
#             if w < 0:
#                 break
#             if match(h, w):
#                 print(h, w)

# rolling hash AC 1.83 #12 1.68 #13 1.62
BASE = 100000007
BASE2 = 1000000007 # don't know why but collision occurs without changing base
MAX = 2**63 - 1

def hash(t: List[int], base=BASE) -> int:
    th = 0
    for i in range(len(t)):
        th = (th * base + t[i]) % MAX
    return th

def hash_table(t: List[int], pl: int, base=BASE) -> List[int]:

    tl = len(t)

    t_pl = base ** pl % MAX
    th = hash(t[:pl], base)
    table = []    
    for i in range(0, tl - pl + 1):
        table.append(th)
        if i + pl < tl:
            th = (th * base + t[i + pl] - t[i] * t_pl) % MAX

    return table

def solve(H: int, W: int, F: List[str], R: int, C: int, P:List[str]) -> None:

    ph = hash([hash([ord(e) for e in r]) for r in P], BASE2)

    th1 = []
    for h in range(H):
        th1.append(hash_table([ord(e) for e in F[h]], C))

    th2: List[List[int]] = [[] for _ in range(H - R + 1)]
    for w in range(W - C + 1):
        colh = hash_table([th1[h][w] for h in range(H)], R, BASE2)
        for h in range(H - R + 1):
            th2[h].append(colh[h])

    for h in range(H - R + 1):
        for w in range(W - C + 1):
            if th2[h][w] == ph:
                print(h, w)
    
H, W = [int(e) for e in stdin.readline().split()]
F = [stdin.readline().strip() for _ in range(H)]
R, C = [int(e) for e in stdin.readline().split()]
P = [stdin.readline().strip() for _ in range(R)]

solve(H, W, F, R, C, P)
