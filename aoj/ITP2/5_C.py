# 5_C.py Permutation

from itertools import permutations

# brute force my own permutation 01.57 s 5604 KB
# brute force itertools 00.05 s 5648 KB
# short code itertools 00.11 s 52372 KB

def solve1(a):

    # def permutations(a):
    #     def rec(p, r):
    #         if len(r) == 0:
    #             yield p
    #         for i in range(len(r)):
    #             p2, r2 = p[:], r[:]
    #             p2.append(r[i])
    #             del r2[i]
    #             yield from rec(p2, r2) 
    #     yield from rec([], a)

    prev = None
    nxt = False
    for p in permutations(sorted(a)):
        if nxt:
            print(*p)
            break
        if p == a:
            if prev is not None:
                print(*prev)
            print(*p)
            nxt = True
        prev = p

def solve2(a):
    perms = list(permutations(sorted(a)))
    i = perms.index(a)
    if i > 0:
        print(*perms[i - 1])
    print(*perms[i])
    if i < len(perms) - 1:
        print(*perms[i + 1])

n = int(input())
a = tuple([int(e) for e in input().split()])

solve2(a)
