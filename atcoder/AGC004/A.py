import sys


def resolve():
    A, B, C = [int(e) for e in sys.stdin.readline().split()]
    if A % 2 == 0 or B % 2 == 0 or C % 2 == 0:
        print(0)
    else:
        print(min(B * C, C * A, A * B))


# resolve()
# exit()
