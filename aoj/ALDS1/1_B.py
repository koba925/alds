# 1_B.py

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

# 実際に使う場合は math.gcd() を使う
# import math
# print(math.gcd(x, y))

x, y = [int(e) for e in input().split()]
print(gcd(x, y))
