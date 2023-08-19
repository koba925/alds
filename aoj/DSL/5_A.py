# 5_A.py The Maximum Number of Customers

from sys import stdin

def solve(n, t, c):
    timeline = [0] * (t + 1)
    for l, r in c:
        timeline[l] += 1
        timeline[r] -= 1

    # First solution
    # count, max_count = 0, 0
    # for i in range(t):
    #     count += timeline[i]
    #     max_count = max(max_count, count)
    # return max_count

    # Cumulative Sum
    count, max_count = 0, 0
    for i in range(t):
        timeline[i + 1] += timeline[i]
    return max(timeline)

n, t = [int(e) for e in stdin.readline().split()]
customers = [
    tuple([int(e) for e in line.split()])
    for line in stdin.readlines()
]

print(solve(n, t, customers))