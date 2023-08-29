# 2次元累積和
def cumulative_sum_2D(H, W, A):
    S = [[0] * (W + 1) for _ in range(H + 1)]
    for r in range(H):
        for c in range(W):
            S[r + 1][c + 1] = S[r][c + 1] + S[r + 1][c] - S[r][c] + A[r][c]
    return S


# 長方形(r1, c1)-(r2, c2)の和（r2,c2)を含む
def get_sum_2D(S, r1, c1, r2, c2):
    return S[r2 + 1][c2 + 1] - S[r1][c2 + 1] - S[r2 + 1][c1] + S[r1][c1]
