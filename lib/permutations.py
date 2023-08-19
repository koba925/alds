def next_permutation_dict_order(p):
    lp = len(p)

    l = lp - 1
    while l > 0 and p[l - 1] >= p[l]: l -= 1
    if l <= 0: return False

    r = lp - 1
    while p[r] <= p[l - 1]: r -= 1
    p[l - 1], p[r] = p[r], p[l - 1]

    p[l:] = p[lp-1:l-1:-1]
    return True

def permutations_dict_order(src):
    p = src[:]
    print(p)
    while next_permutation_dict_order(p):
        print(p)


print("---")
permutations_dict_order([0, 1, 1, 2])

def permutations(src : list):
    def rec(i):
        if i == l:
            print(perm) # do something
            return 

        for j in range(l):
            if used[j]:
                continue
            perm[i] = src[j]
            used[j] = True
            rec(i + 1)
            used[j] = False

    l = len(src)
    used = [False] * l
    perm = [None] * l
    rec(0)

print("---")
permutations([])
print("---")
permutations([1])
print("---")
permutations([1, 2, 3])
print("---")
permutations([1, 1, 2])
