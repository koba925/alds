# 2_B.py

def selection_sort(a):
    exchanges = 0
    for i in range(len(a)):
        minj = i
        for j in range(i, len(a)):
            if a[j] < a[minj]:
                minj = j
        if i != minj:
            a[i], a[minj] = a[minj], a[i]
            exchanges += 1
    return exchanges

n = int(input())
a = [int(e) for e in input().split()]

exchanges = selection_sort(a)
print(*a)
print(exchanges)
