# 3_C.py The Number of Windows

# #20 5.62s #21 TLE
def solve_partial_sum(a, x):
    def calc_sums():
        sum, sums = 0, [0]
        for ai in a:
            sum += ai
            sums.append(sum)
        return sums + [float("inf")]

    def range_sum(start, end):
        return sums[end + 1] - sums[start]

    def solve1(xi):
        count, end = 0, 0
        for start in range(len(a)):
            while range_sum(start, end) <= xi:
                end += 1
            count += (end - start)
        return count

    sums = calc_sums()
    for xi in x:
        print(solve1(xi))

# #20 3.15s #21 TLE
def solve_start_loop(a, x):
    def solve1(xi):
        count, end, sum = 0, 0, a[0]
        for start in range(len(a)):
            while sum <= xi:
                end += 1
                sum += a[end]
            count += (end - start)
            sum -= a[start]
        return count

    a.append(float("inf"))
    for xi in x:
        print(solve1(xi))

# #20 2.71s #21 TLE
def solve_end_loop(a, x):
    def solve1(xi):
        count, start, sum = 0, 0, 0
        for end in range(len(a)):
            sum += a[end]
            while sum > xi:
                sum -= a[start]
                start += 1
            count += end + 1 - start
        return count

    for xi in x:
        print(solve1(xi))

n, q = [int(e) for e in input().split()]
a = [int(e) for e in input().split()]
x = [int(e) for e in input().split()]

# solve_partial_sum(a, x)
# solve_start_loop(a, x)
solve_end_loop(a, x)
