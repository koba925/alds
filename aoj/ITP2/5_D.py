# 5_D.py Permutation Enumeration

# 01.26 s 6344 KB
# from itertools import permutations

# 02.75 s 6308 KB
# def permutations(a):

#     def rec(perm, rest):
#         if rest == []:
#             yield perm
#         else:
#             for i in range(len(rest)):
#                 yield from rec(perm + [rest[i]], rest[:i] + rest[i + 1:])

#     yield from rec([], a)

# 02.97 s 6308 KB
def permutations(a):
    if a == []:
        yield []
    else:
        for i in range(len(a)):
            e = [a[i]]
            for p in permutations(a[:i] + a[i + 1:]):
                yield e + p

# faster but not in lexicographic order (need to be sorted())
# 01.90 s 58540 KB
# def permutations(a):
#     if a == []:
#         yield []
#     else:
#         for p in permutations(a[1:]):
#             e = a[0:1]
#             for i in range(len(p) + 1):
#                 yield p[:i] + e + p[i:] 

n = int(input())
for p in permutations(list(range(1, n + 1))):
    print(*p)
