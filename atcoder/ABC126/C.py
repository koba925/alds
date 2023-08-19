# C - Dice and Coin

from math import log2, ceil

def solve(N, K):
    def prob_numer(dice):
        return 1 if dice >= K else 0.5 ** ceil(log2(K / dice))
    return sum(prob_numer(dice) for dice in range(1, N + 1)) / N

def solve2(N, K):
    def prob_numer(score):
        prob = 1
        while (score < K):
            prob /= 2
            score *= 2
        return prob
        
    return sum(prob_numer(dice) for dice in range(1, N + 1)) / N

N, K = [int(e) for e in input().split()]
print(solve2(N, K))
