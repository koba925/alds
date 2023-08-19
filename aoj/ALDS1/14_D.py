# 14_D.py Multiple String Matching
# TLE #10 0.70s
# TODO

T = input()
Q = int(input())
for _ in range(Q):
    P = input()
    print(1 if T.find(P) != -1 else 0)
