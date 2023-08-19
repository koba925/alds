# A - Two Choices

def solve(_1, _2, solutions):
    def n_pairs(n):
        return n * (n - 1) // 2
    
    parities = [s.count("1") % 2 for s in solutions]
    return parities.count(0) * parities.count(1)

from sys import stdin
N, M = [int(e) for e in stdin.readline().split()]
S = [s.strip() for s in stdin.readlines()]
print(solve(N, M, S))
