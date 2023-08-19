# 10_A.py

def fib(n):
    def rec(k):
        if ans[k] is None:
            ans[k] = rec(k - 1) + rec(k - 2)
        return ans[k]

    ans = [1, 1] + [None] * 43
    return rec(n)

print(fib(int(input())))
