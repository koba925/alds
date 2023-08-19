# 9_A.py

W = input()

T = []
while True:
    s = input()
    if s == "END_OF_TEXT":
        break
    T += s.lower().split()

print(T.count(W))
