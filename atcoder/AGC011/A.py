def resolve():
    N, C, K = [int(e) for e in input().split()]
    T = [int(input()) for _ in range(N)]

    T.sort()
    passengers, buses, first = 0, 0, T[0]

    for t in T:
        if first + K < t:
            passengers = 0
        if passengers == 0:
            buses += 1
            first = t
        passengers += 1
        if passengers == C:
            passengers = 0

    print(buses)

def resolve():
    N, C, K = [int(e) for e in input().split()]
    T = [int(input()) for _ in range(N)]

    T.sort()
    buses = 0

    i = 0
    while i < N:
        buses += 1
        j = i
        while j < min(i + C, N) and T[j] <= T[i] + K:
            j += 1
        i = j
    
    print(buses)

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

    def test_(self):
        input = """7 3 5
    1
    7
    7
    8
    9
    9
    9"""
        output = """3"""
        self.assertIO(input, output)
    

    def test_入力例_1(self):
        input = """5 3 5
1
2
3
6
12"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3 3
7
6
2
8
10
6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
