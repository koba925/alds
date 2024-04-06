import sys
from io import StringIO
import unittest

def resolve_floyd_warshall_TLE():
    from collections import defaultdict

    H, W = [int(e) for e in input().split()]
    S = ["#" * (W + 2)]
    S += ["#" + input() + "#" for _ in range(H)]
    S += ["#" * (W + 2)]

    D = defaultdict(lambda: float("inf"))

    for r in range(1, H + 1):
        for c in range(1, W + 1):
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                D[(r, c, r, c)] = 0
                if S[r][c] == "." and S[r + dr][c + dc] == ".":
                    D[(r, c, r + dr, c + dc)] = 1

    for mr in range(1, H + 1):
        for mc in range(1, W + 1):
            for sr in range(1, H + 1):
                for sc in range(1, W + 1):
                    for tr in range(1, H + 1):
                        for tc in range(1, W + 1):
                            D[(sr, sc, tr, tc)] = min(D[(sr, sc, tr, tc)], D[(sr, sc, mr, mc)] + D[(mr, mc, tr, tc)])
    
    print(max(d for d in D.values() if d != float("inf")))

def resolve_floyd_warshall():
    H, W = [int(e) for e in input().split()]
    S = ["#" * (W + 2)]
    S += ["#" + input() + "#" for _ in range(H)]
    S += ["#" * (W + 2)]

    D = [float("inf")] * ((H + 2) * (W + 2)) ** 2
    pos = lambda r1, c1, r2, c2: ((r1 * W + c1) * H + r2) * W + c2

    for r in range(1, H + 1):
        for c in range(1, W + 1):
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                D[pos(r, c, r, c)] = 0
                if S[r][c] == "." and S[r + dr][c + dc] == ".":
                    D[pos(r, c, r + dr, c + dc)] = 1

    for mr in range(1, H + 1):
        for mc in range(1, W + 1):
            for sr in range(1, H + 1):
                for sc in range(1, W + 1):
                    for tr in range(1, H + 1):
                        for tc in range(1, W + 1):
                            D[pos(sr, sc, tr, tc)] = min(D[pos(sr, sc, tr, tc)], D[pos(sr, sc, mr, mc)] + D[pos(mr, mc, tr, tc)])
    
    print(max(d for d in D if d != float("inf")))

def resolve():
    from collections import deque

    def farthest(sr, sc):
        dist = [[-1] * (W + 2) for _ in range(H + 2)]
        dist[sr][sc] = 0
        to_go = deque()
        to_go.append((sr, sc))

        max_dist = 0
        while to_go:
            r, c = to_go.popleft()
            max_dist = max(max_dist, dist[r][c])
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if S[r + dr][c + dc] == "." and dist[r + dr][c + dc] == -1:
                    dist[r + dr][c + dc] = dist[r][c] + 1
                    to_go.append((r + dr, c + dc))

        return max_dist
    
    H, W = [int(e) for e in input().split()]
    S = ["#" * (W + 2)]
    S += ["#" + input() + "#" for _ in range(H)]
    S += ["#" * (W + 2)]

    max_dist = 0
    for sr in range(1, H + 1):
        for sc in range(1, W + 1):
            if S[sr][sc] == ".":
                max_dist = max(max_dist, farthest(sr, sc))

    print(max_dist)

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """3 3
...
...
..."""
        expected = """4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 5
...#.
.#.#.
.#..."""
        expected = """10"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
