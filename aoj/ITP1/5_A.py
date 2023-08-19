# 5_A.py

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0: break

    for r in range(H):
        for c in range(W):
            print("#", end="");
        print()
    print()
