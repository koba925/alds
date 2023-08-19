# D - Three Days Ago

# naive solution TLE
def solve_naive():
    S = input()
    length = len(S)
    count = 0
    for left in range(length):
        even = [True] * 10
        for right in range(left, length):
            even[int(S[right])] = not even[int(S[right])]
            if all(even):
                count += 1
    print(count)

# Editorial

from collections import defaultdict

def num_pairs(n):
    return n * (n - 1) // 2

def solve():
    S = input()

    counts = defaultdict(int)

    parity = [True] * 10
    counts[tuple(parity)] += 1
    for d in S:
        parity[int(d)] = not parity[int(d)]
        counts[tuple(parity)] += 1

    print(sum(num_pairs(counts[key]) for key in counts))
    

solve()
