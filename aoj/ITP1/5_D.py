# 5_D.py

def include3(x):
    while x > 0:
        if x % 10 == 3:
            return True
        x //= 10
    return False

n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0 or include3(i):
        print(f" {i}", end="")

