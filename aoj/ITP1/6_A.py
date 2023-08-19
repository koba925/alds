# 6_A.py

n = int(input())
a = [int(e) for e in input().split()]

# a.reverse()
# print(" ".join(map(str, a)))

# for i in range(n - 1, -1, -1):
#     if i != n - 1:
#         print(" ", end="")
#     print(a[i], end="")
# print()

for i in range(n):
    if i != 0:
        print(" ", end="")
    print(a[n - i - 1], end="")
print()




