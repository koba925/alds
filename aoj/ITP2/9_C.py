# 16_C.py Set Intersection

n = int(input())
a = {int(e) for e in input().split()}
m = int(input())
b = {int(e) for e in input().split()}

for e in sorted(a - b):
    print(e)
