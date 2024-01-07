def resolve_sortedlist_TLE():
    from sortedcontainers import SortedList

    N, M = [int(e) for e in input().split()]
    A = SortedList(int(e) for e in input().split())

    for _ in range(M):
        b, c = [int(e) for e in input().split()]
        for _ in range(b):
            if A[0] >= c: break
            A.pop(0)
            A.add(c)

    print(sum(A))

def resolve_sorteddict_TLE():
    import collections as cl
    from sortedcontainers import SortedDict

    N, M = [int(e) for e in input().split()]
    A = SortedDict(cl.Counter(int(e) for e in input().split()))

    for _ in range(M):
        b, c = [int(e) for e in input().split()]
        for a in A:
            if b == 0 or a >= c: break
            v = min(A[a], b)
            A[c] = A.get(c, 0) + v
            A[a] -= v 
            b -= v
    
    print(sum(a * n  for a, n in A.items()))

def resolve_heapq_TLE():
    from heapq import heapify, heappush, heappop

    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    heapify(A)

    for _ in range(M):
        b, c = [int(e) for e in input().split()]
        while b > 0:
            a = heappop(A)
            if a >= c: 
                heappush(A, a)
                break
            heappush(A, c)
            b -= 1
    
    print(sum(A))

def resolve_heapq_counter_TLE():
    import collections as cl
    from heapq import heapify, heappush, heappop

    N, M = [int(e) for e in input().split()]
    A = list(cl.Counter(int(e) for e in input().split()).items())
    heapify(A)

    for _ in range(M):
        b, c = [int(e) for e in input().split()]
        while b > 0:
            if A[0][0] >= c: 
                break
            a, n = heappop(A)
            if n > b:
                heappush(A, (a, n - b))
                heappush(A, (c, b))
                b = 0
            else:
                heappush(A, (c, n))
                b -= n
    
    print(sum(a * n  for a, n in A))


def resolve():
    N, M = [int(e) for e in input().split()]
    A = sorted(int(e) for e in input().split())
    BC = [[int(e) for e in input().split()] for _ in range(M)]
    BC = sorted(BC, key=lambda e: e[1], reverse=True)

    ia = 0
    for b, c in BC:
        while b > 0:
            if ia >= N or A[ia] >= c: break
            A[ia] = c
            ia += 1
            b -= 1
    
    print(sum(A))

# resolve()
# exit()


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
        input = """3 2
5 1 4
2 3
1 5"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
1 8 5 7 100 4 52 33 13 5
3 10
4 30
1 4"""
        output = """338"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 2
100 100 100
3 99
3 99"""
        output = """300"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """11 3
1 1 1 1 1 1 1 1 1 1 1
3 1000000000
4 1000000000
3 1000000000"""
        output = """10000000001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
