def resolve_leftside_only_WA():
    import itertools as it

    N, M = [int(e) for e in input().split()]
    X = [int(e) for e in input().split()]
    R = list(sorted((min(a, b), max(a, b)) for a, b in it.pairwise(X)))

    tour = min_tour = sum(b - a for a, b in R)
    i = 0
    for a, b in R:
        tour = tour - (b - a) + (N - (b - a))
        min_tour = min(min_tour, tour)
    print(min_tour)

def resolve_heapq_WA():
    import itertools as it
    from heapq import heappush, heappop

    N, M = [int(e) for e in input().split()]
    X = [int(e) for e in input().split()]

    R = list(sorted((min(a, b), max(a, b)) for a, b in it.pairwise(X)))
    tour = min_tour = sum(b - a for a, b in R)

    hq = []
    for a, b in it.pairwise(X):
        heappush(hq, (a, b))
        heappush(hq, (b, a))

    while hq:
        a, b = heappop(hq)
        if a < b:
            tour = tour - (b - a) + (N - (b - a))
        else:
            tour = tour - (N - (a - b)) + (a - b)
        min_tour = min(min_tour, tour)
    print(min_tour)
        

def resolve_heapq_AC():
    import itertools as it
    from heapq import heappush, heappop

    N, M = [int(e) for e in input().split()]
    X = [int(e) for e in input().split()]

    tour, hq = 0, []
    for s, t in it.pairwise(X):
        l, r = min(s, t), max(s, t)
        tour += (r - l)
        heappush(hq, (l, r))
    min_tour = tour

    while True:
        l, r = heappop(hq)
        if l >= 2 * N: break
        tour = tour - (r - l) + (N - (r - l))
        heappush(hq, (r, N + l))
        min_tour = min(min_tour, tour)

    print(min_tour)


def resolve():
    import itertools as it

    N, M = [int(e) for e in input().split()]
    X = [int(e) - 1 for e in input().split()]

    A = [0] * N
    tour = 0
    for s, t in it.pairwise(X):
        l, r = min(s, t), max(s, t)
        d = r - l
        tour += d
        A[l] += (N - d) - d
        A[r] += d - (N - d)

    min_tour = tour
    for a in A:
        tour += a
        min_tour = min(min_tour, tour)
    print(min_tour)

# editorial imos
def resolve():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    import itertools as it

    N, M = [int(e) for e in input().split()]
    X = [int(e) - 1 for e in input().split()]

    V = [0] * N

    def dist(s, t):
        return t - s if s <= t else t + N - s

    def add(s, t, n):
        if s <= t:
            V[s] += n
            V[t] -= n
        else:
            V[s] += n
            V[0] += n
            V[t] -= n
    
    for s, t in it.pairwise(X):
        add(s, t, dist(t, s))
        add(t, s, dist(s, t))
    
    print(min(it.accumulate(V)))    


# resolve()
# exit()



import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 3
1 3 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5
2 4 2 4 2"""
        output = """8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """163054 10
62874 19143 77750 111403 29327 56303 6659 18896 64175 26369"""
        output = """390009"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
