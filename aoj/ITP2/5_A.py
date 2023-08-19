# 5_A.py Sorting Pairs

from sys import stdin, stdout

n = int(stdin.readline())

# points = []
# for _ in range(n):
#     points.append(tuple([int(e) for e in stdin.readline().split()]))

# faster and less memory than list and readlines()
points = [
    tuple([int(e) for e in stdin.readline().split()])
    for _ in range(n)    
]

# points = [
#     tuple([int(e) for e in l.split()])
#     for l in stdin.readlines()    
# ]

# for p in sorted(points):
#     print(*p)

# stdout.writelines(f"{p[0]} {p[1]}\n" for p in sorted(points))

# less memory than sorted()
points.sort()
stdout.writelines(f"{p[0]} {p[1]}\n" for p in points)
