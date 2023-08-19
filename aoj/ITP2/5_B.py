# 5_B.py Sorting Tuples

from sys import stdin, stdout

n = int(stdin.readline())

# imperative
# 00.61 s 32100 KB
# things = []
# for _ in range(n):
#     v, w, t, d, s = stdin.readline().split()
#     things.append((int(v), int(w), t, int(d), s))

# shorter and readable, but use twice as much memory
# 00.55 s 66892 KB
# things = [l.split() for l in stdin.readlines()]
# things = [(int(v), int(w), t, int(d), s) for v, w, t, d, s in things]

# 1 line solution with readline() and generator
# 00.56 s 32096 KB
things = [
    (int(v), int(w), t, int(d), s) for v, w, t, d, s in (
        stdin.readline().split() for _ in range(n)
    )
]

for t in sorted(things):
    print(*t)
