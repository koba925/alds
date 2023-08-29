# import sys
# def debug(*args, **kwargs):
#     print(*args, **kwargs, file=sys.stderr)

import itertools as it


# N個あるAのうちK個を取る組み合わせをすべて試す
def try_combinations_selfcoding(N, K, A):
    def _combinations(i, n, total):
        nonlocal result
        # debug(i, n, total, used)
        if n == K:
            result = min(result, total)
            return
        if i + (K - n) > N:
            return
        _combinations(i + 1, n, total)
        # used[i] = True
        _combinations(i + 1, n + 1, total + A[i])
        # used[i] = False

    # used = [False] * N
    result = float("inf")
    _combinations(0, 0, 0)
    return result


def try_combinations(N, K, A):
    result = float("inf")
    for c in it.combinations(A, K):
        result = min(result, sum(c))
    return result


def test():
    for N in range(5):
        for K in range(0, N + 1):
            for A in it.permutations(range(1, N + 1)):
                result = try_combinations(N, K, A)
                assert result == K * (K + 1) // 2


test()
