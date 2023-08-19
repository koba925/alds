# 5_B.py

def drawline(w, c, end="\n"):
    for i in range(w):
        print(c, end="")
    print("", end=end)    

def drawRectangle(h, w):
    drawline(w, "#")
    for r in range(h - 2):
        print("#", end="")
        drawline(w - 2, ".", end="")
        print("#")
    drawline(w, "#")

while True:
    H, W = [int(e) for e in input().split()]
    if H == 0 and W == 0: break
    drawRectangle(H, W)
    print()
