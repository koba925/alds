# Q03.py

cards = [False] * 101 # 1-based

for n in range(2, 101):
    for k in range(n, 101, n):
        cards[k] = not cards[k]
print([i for i in range(1, 101) if not cards[i]])
    