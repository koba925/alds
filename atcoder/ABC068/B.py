
def div_2_times(n):
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

def solve_1():
    N = int(input())
    print(max((div_2_times(n), n) for n in range(1, N + 1))[1])

from itertools import count, takewhile

def solve():
    N = int(input())
    print(list(takewhile(lambda n: n <= N, (2 ** n for n in count())))[-1])

solve()
