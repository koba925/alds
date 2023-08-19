# A - ><

def solve_mine(S):
    N = len(S) + 1
    a = [0] + [0] * N + [0]         # 1-based + centinel
    S = ">" + S + "<"               # centinel
    for i in range(1, N + 1):
        if S[i - 1] == "<":
            a[i] = a[i - 1] + 1
    for i in reversed(range(1, N + 1)):
        if S[i] == ">":
            a[i] = max(a[i], a[i + 1] + 1) 
    return sum(a)

def solve(S):
    N = len(S) + 1
    a = [0] * N
    for i in range(1, N):
        if S[i - 1] == "<":
            a[i] = a[i - 1] + 1
    for i in reversed(range(N - 1)):
        if S[i] == ">":
            a[i] = max(a[i], a[i + 1] + 1) 
    return sum(a)

print(solve(input()))
