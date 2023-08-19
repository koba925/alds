# 10_A.py Bit Operation I

x = int(input())

print(f"{x:032b}")
print(f"{x ^ 0xffffffff:032b}")
print(f"{x << 1 & 0xffffffff:032b}")
print(f"{x >> 1:032b}")
