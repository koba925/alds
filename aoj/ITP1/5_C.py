# 5_C.py

def drawRectangle(height, width):
    for r in range(height):
        for w in range(width):
            print("#" if (r + w) % 2 == 0 else ".", end="")
        print()


while True:
    H, W = [int(e) for e in input().split()]
    if H == 0 and W == 0:
        break
    drawRectangle(H, W)
    print()
