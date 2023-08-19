# 1_A.py

def insertion_sort(a):
    for i in range(1, len(a)):
        v = a[i]
        j = i - 1
        while j >= 0 and a[j] > v:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = v
        print(*a)

n = int(input())
a = [int(e) for e in input().split()]
print(*a) # ここで一回出力しておけば1からループ開始してもAC
insertion_sort(a)
