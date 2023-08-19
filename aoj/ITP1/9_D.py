# 9_D.py

s = input()
q = int(input())

for i in range(q):
    c, a, b, *p = input().split()
    a = int(a)
    b = int(b)
    if c == "replace":
        s = s[:a] + p[0] + s[b+1:]
    elif c == "reverse":
        s = s[:a] + s[a:b+1][::-1] + s[b+1:]
    elif c == "print":
        print(s[a:b+1])
