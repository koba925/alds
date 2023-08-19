# C - Rectangle Cutting

def solve(W, H, x, y):
    max_area = W * H / 2
    division = 1 if W / 2 == x and H / 2 == y else 0
    print(max_area, division)

W, H, x, y = [int(e) for e in input().split()]
solve(W, H, x, y)