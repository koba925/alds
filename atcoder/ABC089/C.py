# C - March

def solve(N, names):
    def _solve(k, u, ans):
        if u == 3:
            return ans
        if k == 5 or ans == 0:
            return 0
        return _solve(k + 1, u, ans) + _solve(k + 1, u + 1, ans * n[k])
         
    n = []
    for initial in ("M", "A", "R", "C", "H"):
         n.append(len([name for name in names if name.startswith(initial)]))

    # return _solve(0, 0, 1)

    ans = 0
    for i in range(len(n) - 2):
        for j in range(i + 1, len(n) - 1):
            for k in range(j + 1, len(n)):
                ans += n[i] * n[j] * n[k]
    return ans

N = int(input())
S = [input() for _ in range(N)]
print(solve(N, S))
