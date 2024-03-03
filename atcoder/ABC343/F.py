def resolve():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    from atcoder.segtree import SegTree

    MAXVAL = 2**31 - 1

    import collections as cl

    def merge(d1: dict[int, int], d2: dict[int, int]):
        ret = {}
        for k in set(d1.keys()).union(d2.keys())
            ret[k] = d1.get(k, 0) + d2.get(k, 0)
        return ret

    N, Q = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    ST = SegTree(merge, {}, {a: 1 for a in A})

    for _ in range(Q):
        com, x, y = [int(e) for e in input().split()]
        match com:
            case 0: A.set(x, y)
            case 1: print(A.prod(x, y + 1))
    def solve():
        return
    
    
    print(solve())

# resolve()
# exit()

