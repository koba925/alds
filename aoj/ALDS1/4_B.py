# 4_B.py

def binary_search(e, S):
    left = 0
    right = len(S)
    while right - left > 1:
        mid = (left + right) // 2
        if S[mid] < e:
            left = mid
        else:
            right = mid
    return right if S[right] == e else -1

n = int(input())
S = [int(e) for e in input().split()]
S.sort()
q = int(input())
T = [int(e) for e in input().split()]

print(len([e for e in T if binary_search(e, S) >= 0]))
