# 10_C.py

def longest_common_subsequence(x, y):
    table = [0] * (len(y) + 1)

    for i in range(len(x)):
        prev = table[:]
        X = x[i]
        for j in range(len(y)):
            if X == y[j]:
                table[j + 1] = prev[j] + 1
            elif table[j + 1] < table[j]:
                table[j + 1] = table[j]

    return table[-1]

q = int(input())

for _ in range(q):
    x = input()
    y = input()
    print(longest_common_subsequence(x, y))
