# bit DP

# Travelling Salesman Problem
# https://qiita.com/drken/items/7c6ff2aa4d8fce1c9361#11-bit-dp
# TODO: solve it by DP


def travelling_salesman_recursive():
    MAX_CITY = 10

    def solve(N, G):
        def rec(bit, v):
            if dp[bit][v] != -1:
                return dp[bit][v]

            if bit == (1 << v):
                dp[bit][v] == 0
                return 0

            min_dist = float("inf")
            prev_bit = bit & ~(1 << v)

            for u in range(N):
                if not (prev_bit & (1 << u)):
                    continue
                dist = rec(prev_bit, u) + G[u][v]
                min_dist = min(min_dist, dist)

            dp[bit][v] = min_dist
            return min_dist

        dp = [[-1] * N for _ in range(1 << N)]
        min_dist = float("inf")
        for v in range(N):
            min_dist = min(min_dist, rec((1 << N) - 1, v))
        return min_dist

    print(solve(3, [[0, 5, 2], [5, 0, 4], [2, 4, 0]]))
    print(solve(4, [[0, 8, 7, 3], [8, 0, 9, 1], [7, 9, 0, 4], [3, 1, 4, 0]]))
