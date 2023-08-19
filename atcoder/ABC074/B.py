from sys import stdin

def collect(N, K, X):
    return sum(min(x, K - x) for x in X) * 2

def solve():
    N = int(stdin.readline())
    K = int(stdin.readline())
    X = [int(e) for e in stdin.readline().split()]

    print(collect(N, K, X))

solve()
