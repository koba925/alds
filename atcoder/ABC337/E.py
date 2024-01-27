def resolve():
    N = int(input())

    M = 0
    while 2 ** M < N:
        M += 1

    print(M)

    K = [[] for _ in range(M)]
    for i in range(N):
        ibin = f"{i:0{M}b}"
        for j in range(M):
            if ibin[j] == "1": K[j].append(i + 1)

    for j in range(M):
        print(len(K[j]), *K[j])
    
    S = input()
    print(int(S, base=2) + 1)

def resolve():
    N = int(input())

    M = 0
    while 2 ** M < N:
        M += 1

    print(M)

    K = [[] for _ in range(M)]
    for i in range(N):
        b = i
        for j in range(M):
            if b & 1 == 1: K[j].append(i + 1)
            b >>= 1

    for j in range(M):
        print(len(K[j]), *K[j])
    
    S = input()
    ans = 0
    for s in S[::-1]:
        ans <<= 1
        if s == "1": ans += 1
    print(ans + 1)

resolve()
# exit()

