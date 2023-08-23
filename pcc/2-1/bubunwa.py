def dfs(a, k):
    def _dfs(i, s):
        if i == l:
            return s == k
        if _dfs(i + 1, s):
            return True
        if _dfs(i + 1, s + a[i]):
            return True
        return False

    l = len(a)
    return _dfs(0, 0)


a = [1, 2, 4, 7]
k = 13

print("Yes" if dfs(a, k) else "No")
