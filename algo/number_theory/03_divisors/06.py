import sys  # https://docs.python.org/ja/3/library/sys.html


def divisors_of(N) -> list:
    i, divisors = 1, []
    while i * i <= N:
        if N % i == 0:
            divisors.append(i)
            if N // i != i:
                divisors.append(N // i)
        i += 1
    return sorted(divisors)


def resolve():
    A, B = [int(e) for e in sys.stdin.readline().split()]
    print(len(divisors_of(abs(A - B))))


resolve()
# exit()
