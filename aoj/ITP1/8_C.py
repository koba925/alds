# 8_C.py

from sys import stdin

f = [0] * 26

s = stdin.read()
for c in s:
    if c.isalpha():
        f[ord(c.lower()) - ord("a")] += 1

for i in range(26):
    print(f"{chr(ord('a') + i)} : {f[i]}")
