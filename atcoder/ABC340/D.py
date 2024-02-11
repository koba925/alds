def resolve():
    from heapq import heappush, heappop

    N = int(input())
    G = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b, x = [int(e) for e in input().split()]
        G[i].append((i + 1, a))
        G[i].append((x - 1, b))

    MAX = 10 ** 20
    hq = []
    dist = [MAX] * N
    dist[0] = 0
    heappush(hq, (0, 0))

    while hq:
        d, id = heappop(hq)
        for a, w in G[id]:
            if (d + w < dist[a]):
                dist[a] = d + w
                heappush(hq, (d + w, a))

    print(dist[N - 1])

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
        input = """5
100 200 3
50 10 1
100 200 5
150 1 2"""
        output = """350"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1000 10 9
1000 10 10
1000 10 2
1000 10 3
1000 10 4
1000 10 5
1000 10 6
1000 10 7
1000 10 8"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1000000000 1000000000 1
1000000000 1000000000 1
1000000000 1000000000 1
1000000000 1000000000 1
1000000000 1000000000 1"""
        output = """5000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
