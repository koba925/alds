# 7_C.py

maxr, maxc = [int(e) for e in input().split()]
m = [[]] * (maxr + 1)
for i in range(maxr):
    m[i] = [int(e) for e in input().split()] + [0]
m[maxr] = [0] * (maxc + 1)

for i in range(maxr):
    for j in range(maxc):
        m[i][maxc] += m[i][j]
        m[maxr][j] += m[i][j]
        m[maxr][maxc] += m[i][j]

for r in m:
    print(*r)
