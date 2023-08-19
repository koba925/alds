def bubble_sort(a):
    for i in reversed(range(len(a))):
        exchanged = False
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                exchanged = True
        if not exchanged:
            break

def bubble_sort(a, f = lambda x: x):
    for i in reversed(range(len(a))):
        exchanged = False
        for j in range(0, i):
            if f(a[j]) > f(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                exchanged = True
        if not exchanged:
            break

def selection_sort(a):
    for i in range(len(a)):
        minj = i
        for j in range(i, len(a)):
            if a[j] < a[minj]:
                minj = j
        if i != minj:
            a[i], a[minj] = a[minj], a[i]

def shell_sort(a):
    def insertion_sort(a, gi):
        for i in range(gi, n):
            v = a[i]
            j = i - gi
            while j >= 0 and a[j] > v:
                a[j + gi] = a[j]
                j -= gi
            a[j + gi] = v

    g = [797161, 265720, 88573, 29524, 9841, 3280, 1093, 364, 121, 40, 13, 4, 1]
    for gi in g:
        insertion_sort(a, gi)

from math import inf

def mergesort(A):
    def merge(left, mid, right):

        L = A[left:mid] + [inf]
        R = A[mid:right] + [inf]
        i, j = 0, 0
        for k in range(left, right):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1

    def rec(left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            rec(left, mid)
            rec(mid, right)
            merge(left, mid, right)

    rec(0, len(A))

def mergesort(a, f=lambda x: x, l=inf):

    def merge(left, mid, right):
        L = a[left:mid] + [l]
        R = a[mid:right] + [l]
        i, j = 0, 0
        for k in range(left, right):
            if f(L[i]) <= f(R[j]):
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1

    def rec(left, right):
        if left + 1 < right:
            mid = (left + right) // 2
            rec(left, mid)
            rec(mid, right)
            merge(left, mid, right)

    rec(0, len(a))


def quicksort(a, f=lambda x: x):
    def partition(p, r):
        x = a[r]
        i = p
        for j in range(p, r):
            if f(a[j]) <= f(x):
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[r] = a[r], a[i]
        return i

    def rec(p, r):
        if p < r:
            q = partition(p, r)
            rec(p, q - 1)
            rec(q + 1, r)

    rec(0, len(a) - 1)