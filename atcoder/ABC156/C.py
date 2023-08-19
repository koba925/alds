# ABC156C Rally

def solve(N, X):
    return min(sum(((xi - P) ** 2 for xi in X)) for P in range(1, 101))

from sys import stdin

N = int(stdin.readline())
X = [int(e) for e in stdin.readline().split()]
print(solve(N, X))

