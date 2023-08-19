# B - Can you solve this?

def solve(N, M, C, B, A):
    def score(Ai):
        return sum(Ai[m] * B[m] for m in range(M)) + C

    return len([1 for Ai in A if score(Ai) > 0])

N, M, C = [int(e) for e in input().split()]
B = [int(e) for e in input().split()]
A = [[int(e) for e in input().split()] for _ in range(N)]

print(solve(N, M, C, B, A))
