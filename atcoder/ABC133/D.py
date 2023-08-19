from sys import stdin

def rainfalls_naive(N, A):
    rainfalls_total = sum(A)
    for r1 in range(0, rainfalls_total // 2 + 1, 2):
        R = [0] * N
        R[0] = r1 
        for i in range(1, N):
            R[i] = 2 * A[i - 1] - R[i - 1]
            if R[i] < 0:
                break
        else:
            if R[0] == 2 * A[N - 1] - R[N - 1]:
                break
    return R

def rainfalls(N, A):
    S = sum(A)

    R = [S - 2 * sum(A[i] for i in range(1, N - 1) if i % 2 == 1)]

    for i in range(1, N):
        R.append(2 * A[i - 1] - R[i - 1])

    return R

def solve():
    N = int(stdin.readline())
    A = [int(e) for e in stdin.readline().split()]

    print(*rainfalls(N, A))


solve()
