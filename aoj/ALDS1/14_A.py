# 14_A.py
# startswith: AC 0.01s - 0.02s
# naive: AC 0.01s - 0.02s

T = input()
P = input()

for i in range(len(T) - len(P) + 1):
    for j in range(len(P)):
        if T[i + j] != P[j]:
            break
    else:
        print(i)
