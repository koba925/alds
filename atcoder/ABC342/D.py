def resolve_contest():

    import collections as cl

    def prime_factorize(N):
        factors = []
        n = 2
        while n * n <= N:
            if N % n == 0:
                p = 0
                while N % n == 0:
                    N //= n
                    p += 1
                factors.append((n, p))
            n += 1
        if N != 1:
            factors.append((N, 1))
        return factors

    def parity_pattern(N):
        return () if N == 0 else tuple(n for n, p in prime_factorize(N) if p % 2 == 1)

    def solve(N, A):
        Z = A.count(0)
        A = [a for a in A if a != 0]
        B = [parity_pattern(a) for a in A]
        C = cl.Counter(B)
        D = [c * (c - 1) // 2 for c in C.values()]
        return sum(D) + Z * (N - 1) - Z * (Z - 1) // 2
 
    N, A = int(input()), [int(e) for e in input().split()]
    print(solve(N, A))

def resolve_2():
    import collections as cl

    def divide_squares(a):
        n = 2
        nsq = n * n
        while nsq <= a:
            if a % nsq == 0:
                a //= nsq
            else:
                n += 1
                nsq = n * n
        return a
    
    def solve(N, A):
        R = [divide_squares(a) for a in A]
        C = cl.Counter(R)
        Z = C[0]
        del C[0]
        return Z * (N - 1) - Z * (Z - 1) // 2 + sum([c * (c - 1) // 2 for c in C.values()])
    
    print(solve(int(input()), [int(e) for e in input().split()]))

def resolve_TLE():
    import collections as cl

    def divide_squares(a):
        for n in range(1000, 1, -1):
            nsq = n * n
            if a % nsq == 0:
                a //= nsq
        return a
    
    def solve(N, A):
        R = [divide_squares(a) for a in A]
        C = cl.Counter(R)
        Z = C[0]
        del C[0]
        return Z * (N - 1) - Z * (Z - 1) // 2 + sum([c * (c - 1) // 2 for c in C.values()])
    
    print(solve(int(input()), [int(e) for e in input().split()]))

def resolve():
    import collections as cl

    MAXA = 2 * 10 ** 5 + 1
    
    def solve(N, A):
        table = list(range(MAXA))
        for n in range(int(MAXA ** 0.5) + 1, 1, -1):
            nsq = n * n
            for m in range(nsq, MAXA, nsq):
                if table[m] % nsq == 0: table[m] //= nsq

        R = [table[a] for a in A]
        C = cl.Counter(R)
        Z = C[0]
        del C[0]
        return Z * (N - 1) - Z * (Z - 1) // 2 + sum([c * (c - 1) // 2 for c in C.values()])
    
    print(solve(int(input()), [int(e) for e in input().split()]))


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

    def test_my_1(self):
        input = """3
0 0 0"""
        output = """3"""
        self.assertIO(input, output)

    def test_my_2(self):
        input = """4
1 1 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_my_3(self):
        input = """4
1 1 4 2"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """5
0 3 2 8 12"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
2 2 4 6 3 100 100 25"""
        output = """7"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
