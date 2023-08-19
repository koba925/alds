# 10_D.py

def minkow(p, x, y):
    return sum(abs(xi - yi) ** p for xi, yi in zip(x, y)) ** (1 / p)

def cheby(x, y):
    return max(abs(xi - yi) for xi, yi in zip(x, y))

n = int(input())
x = [int(e) for e in input().split()]
y = [int(e) for e in input().split()]

print(minkow(1, x, y))
print(minkow(2, x, y))
print(minkow(3, x, y))
print(cheby(x, y))
