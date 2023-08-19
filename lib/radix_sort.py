def radix_sort(A):
    n = len(A)
    if n == 0:
        return

    max_value = max(A)
    max_digits = len(str(max_value))
    for i in range(max_digits):
        bins = [[] for _ in range(10)]
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            bins[e].append(A[j])
        k = 0
        for x in range(10):
            for y in range(len(bins[x])):
                A[k] = bins[x][y]
                k += 1


### from udemy


def radixsort(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    l = []
    bins = [l] * 10
    for i in range(digits):
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x].pop(0)
                    k = k + 1


def radixsort2(A):
    n = len(A)
    maxelement = max(A)
    digits = len(str(maxelement))
    for i in range(digits):
        l = []
        bins = [l] * 10
        for j in range(n):
            e = int((A[j] / pow(10, i)) % 10)
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            if len(bins[x]) > 0:
                for y in range(len(bins[x])):
                    A[k] = bins[x][y]
                    k = k + 1


import timeit

A = [63, 250, 835, 947, 651, 28]
print(timeit.timeit("radixsort(A)", globals=globals(), number=10))
print(A)

A = [63, 250, 835, 947, 651, 28]
print(timeit.timeit("radixsort2(A)", globals=globals(), number=10))
print(A)

for i in range(10000, 100000, 10000):
    A = [12345] * i
    print(timeit.timeit("radixsort(A)", globals=globals(), number=1))
    print(timeit.timeit("radixsort2(A)", globals=globals(), number=1))


[1, 1, 1, 2, 3].count(1)
"bcabb".count("b")
