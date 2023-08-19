# 4_A.py

n = int(input())
S = {int(e) for e in input().split()}
q = int(input())
T = {int(e) for e in input().split()}

print(len(S & T))
