# A - XOR Circle

# TLE & WA
def solve_TLE_WA(N, A):
    for second in range(1, N):
        camels = [A[0], A[second]]
        rest = set(A[1:])
        xor = A[0] ^ A[second]
        rest.discard(A[second])
        while rest:
            if xor in rest:
                camels.append(xor)
                xor ^= camels[-2]
                rest.discard(camels[-1])
            else:
                break
        else:
            if xor == A[0]:
                return "Yes"
    return "No"

# After Editorial

from collections import Counter

def solve(N, A):
    c = Counter(A)
    ks, vs = list(c.keys()), list(c.values())

    if c[0] == N:
        return "Yes"
    if len(ks) == 2 and c[0] == N // 3:
        return "Yes"
    if len(ks) == 3 and \
       all(v == N // 3 for v in vs) and \
       ks[0] ^ ks[1] ^ ks[2] == 0:
        return "Yes"
    return "No"

N = int(input())
A = [int(e) for e in input().split()]
print(solve(N, A))
