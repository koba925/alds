# 16_A.py Set Union

n = int(input())
a = {int(e) for e in input().split()}
m = int(input())
b = {int(e) for e in input().split()}

print(*sorted(a | b), sep="\n")
