# B - Tax Rate

def divceil(a, x): return -(-a // x)

def solve1(N):
    f = int(N // 1.08)
    c = int(divceil(N, 1.08))
    if int(f * 1.08) == N:
        print(f)
    elif int(c * 1.08) == N:
        print(c)
    else:
        print(":(")

def solve2(N):
    for m in range(1, 50000):
        if int(m * 1.08) == N:
            print(m)
            return
    print(":(")

def solve3(N):
    c = int(divceil(N, 1.08))
    if int(c * 1.08) == N:
        print(c)
    else:
        print(":(")

solve3(int(input()))
