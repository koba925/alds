# 10_A.py

def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

x1, y1, x2, y2 = [float(e) for e in input().split()]
print(distance(x1, y1, x2, y2))
