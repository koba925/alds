# TK: 1レベルまとめて処理することで何歩めか知っているBFS

import sys
from io import StringIO
import unittest

def resolve():
    import collections as cl

    def maze(H, W, S):
        path = "snuke"

        to_go = cl.deque()
        visited = [[False] * W for _ in range(H)]

        if S[0][0] != "s": return False

        to_go.append((0,0))
        visited[0][0] = True
        step = 0

        while to_go:
            n_to_go = len(to_go)
            step += 1
            for _ in range(n_to_go):
                row, col = to_go.popleft()
                if row == H - 1 and col == W - 1: return True
                for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nrow, ncol = row + drow, col + dcol
                    if (0 <= nrow < H and 0 <= ncol < W and
                        not visited[nrow][ncol] and
                        S[nrow][ncol] == path[step % len(path)]):
                        visited[nrow][ncol] = True
                        to_go.append((nrow, ncol))
        return False

    H, W = [int(e) for e in input().split()]
    S = [input() for _ in range(H)]
    print("Yes" if maze(H, W, S) else "No")

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """2 3
sns
euk"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """2 2
ab
cd"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """5 7
skunsek
nukesnu
ukeseku
nsnnesn
uekukku"""
        expected = """Yes"""
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
