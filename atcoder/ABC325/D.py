def resolve():
    import itertools as it    
    from heapq import heappush, heappop

    heaptop = lambda hq: hq[0]
    heapempty = lambda hq: len(hq) == 0

    N = int(input())
    items = []
    for _ in range(N):
        t, d = [int(e) for e in input().split()]
        items.append((t, t + d))
    items.sort()

    count = 0

    t = 0
    i = 0
    q = []
    while i < N or not heapempty(q):
        while i < N and items[i][0] == t:
            heappush(q, items[i][1])
            i += 1
        while not heapempty(q):
            e = heappop(q)
            if t <= e:
                count += 1
                t += 1
                break
        if heapempty(q) and i < N:
            t = items[i][0]

    print(count)


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

    def test_1(self):
        input = """2
1 1
2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_2(self):
        input = """2
1 1
3 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_3(self):
        input = """2
1 1
1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_4(self):
        input = """3
1 1
1 1
1 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """5
1 1
1 1
2 1
1 2
1 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
1 1
1000000000000000000 1000000000000000000"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
4 1
1 2
1 4
3 2
5 1
5 1
4 1
2 1
4 1
2 4"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
