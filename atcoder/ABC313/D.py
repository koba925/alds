# LL: インタラクティブ問題ではprintにflush=Trueを指定する（しないとTLE）

import sys


def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]

    A = [None] * (N + 1)
    T = [None] * (N + 1)

    for i in range(1, K + 2):
        print("?", *range(1, i), *range(i + 1, K + 2), flush=True)
        T[i] = int(sys.stdin.readline())
        if T[i] == -1:
            sys.exit()

    T1 = sum(T[1 : K + 2]) % 2
    for i in range(1, K + 2):
        A[i] = (T1 + T[i]) % 2

    for i in range(K + 2, N + 1):
        print("?", *range(1, K), i, flush=True)
        T[i] = int(sys.stdin.readline())
        if T[i] == -1:
            sys.exit()

    T2 = sum(T[1:K]) % 2
    for i in range(K + 2, N + 1):
        A[i] = (T[i] + T2) % 2

    print("!", *A[1:], flush=True)


resolve()
