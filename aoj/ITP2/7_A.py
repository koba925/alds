# 7_A.py Set: Search

from sys import stdin

q = int(stdin.readline())
s = set()
for query in stdin.readlines():
    command, param = [int(e) for e in query.split()]
    if command == 0:
        s.add(param)
        print(len(s))
    else:
        print(1 if param in s else 0)
