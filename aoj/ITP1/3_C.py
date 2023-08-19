# 3_C.py

# while True:
#     x, y = [int(e) for e in input().split()]
#     if x == 0 and y == 0: break
#     if x > y: x, y = y, x
#     print(x, y)

import sys

for l in list(sys.stdin):
    print(l.rstrip())

    

