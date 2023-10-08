from heapq import heappush, heappop
heaptop = lambda hq: hq[0]
heapempty = lambda hq: len(hq) == 0

def resolve():
    N = int(input())
    S = []

    for _ in range(N):
        s, c = [int(e) for e in input().split()]
        heappush(S, (s, c))

    slimes = 0
    while not heapempty(S):
        s, c = heappop(S)
        while not heapempty(S):
            nexts, nextc = heaptop(S)
            if nexts != s:
                break
            c += nextc
            heappop(S)
        slimes += c % 2
        if c >= 2:
            heappush(S, (s * 2, c // 2))

    print(slimes)

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
        input = """3
3 3
5 1
6 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
1 1
2 1
3 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
1000000000 1000000000"""
        output = """13"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
