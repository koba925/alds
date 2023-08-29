# ナップサック問題では通常横軸にWを取るが、Vを取って計算することも可能
# 問題に合わせて使う
# 横軸がW（値がV） → 与えられた制約内で最大の価値を実現する
# 横軸がV（値がW） → 最小限のコストで与えられた価値を満たす
# 参照：knapsack_dp_transpose


def knapsack_recursive(N, W, V, L):
    def rec(i, w):
        if memo[i][w] != -1:
            return memo[i][w]

        if i == N:
            ret = 0
        elif w + W[i] > L:
            ret = rec(i + 1, w)
        else:
            ret = max(rec(i + 1, w), rec(i + 1, w + W[i]) + V[i])

        memo[i][w] = ret
        return ret

    memo = [[-1] * (L + 1) for _ in range(N + 1)]
    ret = rec(0, 0)
    print(*memo, sep="\n")
    return ret


def knapsack_reverse_recursive(N, W, V, L):
    def rec(i, w):
        if memo[i][w] != -1:
            return memo[i][w]

        if i == N:
            ret = 0
        elif w < W[i]:
            ret = rec(i + 1, w)
        else:
            ret = max(rec(i + 1, w), rec(i + 1, w - W[i]) + V[i])

        memo[i][w] = ret
        return ret

    memo = [[-1] * (L + 1) for _ in range(N + 1)]
    ret = rec(0, L)
    print(*memo, sep="\n")
    return ret


def knapsack_dp_2D(N, W, V, L):
    memo = [[-1] * (L + 1) for _ in range(N + 1)]
    for w in range(L + 1):
        memo[N][w] = 0

    for i in reversed(range(N)):
        for w in range(L + 1):
            memo[i][w] = memo[i + 1][w]
            if W[i] <= w:
                memo[i][w] = max(memo[i][w], memo[i + 1][w - W[i]] + V[i])

    print(*memo, sep="\n")
    return memo[0][L]


def knapsack_dp(N, W, V, L):
    memo = [0] * (L + 1)
    for i in reversed(range(N)):
        for w in reversed(range(L + 1)):
            if W[i] <= w:
                memo[w] = max(memo[w], memo[w - W[i]] + V[i])
        print(memo)
    return memo[L]


def knapsack_dp_transpose(N, W, V, L):
    vtotal = sum(V)
    memo = [0] + [float("inf")] * vtotal
    for i in reversed(range(N)):
        for v in reversed(range(vtotal + 1)):
            if v >= V[i]:
                memo[v] = min(memo[v], memo[v - V[i]] + W[i])
        print(memo)
    return [i for i, w in enumerate(memo) if w <= L][-1]


def resolve():
    N = 4
    W, V = zip(*[(2, 3), (1, 2), (3, 4), (2, 2)])
    L = 5

    print(knapsack_recursive(N, W, V, L))
    print(knapsack_reverse_recursive(N, W, V, L))
    print(knapsack_dp_2D(N, W, V, L))
    print(knapsack_dp(N, W, V, L))
    print(knapsack_dp_transpose(N, W, V, L))


resolve()
