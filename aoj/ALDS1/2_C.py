# 2_C.py

def bubble_sort(c):
    for i in range(len(c)):
        for j in reversed(range(i + 1, len(c))):
            if c[j]["value"] < c[j - 1]["value"]:
                c[j], c[j - 1] = c[j - 1], c[j]

def selection_sort(c):
    for i in range(len(c)):
        minj = i
        for j in range(i, len(c)):
            if c[j]["value"] < c[minj]["value"]:
                minj = j
        c[i], c[minj] = c[minj], c[i]

n = int(input())
cb = [{ "suit": e[0], "value": int(e[1])} for e in input().split()]
cs = cb.copy()

bubble_sort(cb)
selection_sort(cs)

print(*[e["suit"] + str(e["value"]) for e in cb])
print("Stable")
print(*[e["suit"] + str(e["value"]) for e in cs])
print("Stable" if cb == cs else "Not stable")

