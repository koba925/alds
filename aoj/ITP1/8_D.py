# 8_D.py

s = input()
ss = s + s
p = input()

for i in range(len(s)):
    for j in range(len(p)):
        if ss[i + j] != p[j]:
            break
    else:
        print("Yes")
        break
else:
    print("No")
