# 2_A.py

def bubble_sort(a):
    exchanges = 0
    for i in reversed(range(len(a))):
        exchanged = False
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                exchanges += 1
                exchanged = True
        if not exchanged:
            break
    return exchanges

n = int(input())
a = [int(e) for e in input().split()]

exchanges = bubble_sort(a)
print(*a)
print(exchanges)
