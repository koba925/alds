# 3_D.py Lexicographical Comparison

def lexical_comparison(a, b):
    for i in range(min(len(a), len(b))):
        if a[i] > b[i]:
            return 0
        elif b[i] > a[i]:
            return 1
    return 0 if i == len(b) - 1 else 1

from sys import stdin

n = int(stdin.readline())
a = [int(e) for e in stdin.readline().split()]
m = int(stdin.readline())
b = [int(e) for e in stdin.readline().split()]

print(lexical_comparison(a, b))
