import sys
from io import StringIO
import unittest

def resolve():
    import sys
    sys.setrecursionlimit(1000000)

    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    def solve_rec_TLE(N, H, AB):
        def _solve(n, h):
            nonlocal keep

            if h <= 0:
                return n

            minn = float("inf")
            for i in keep.copy():
                keep.remove(i)
                minn = min(minn, _solve(n + 1, h - AB[i][1]))
                keep.add(i)
                minn = min(minn, _solve(n + 1, h - AB[i][0]))
            return minn

        keep = set(range(N))
        return _solve(0, H)

    N, H = [int(e) for e in input().split()]
    AB = [[int(e) for e in input().split()] for _ in range(N)]
    print(solve(N, H, AB))

def resolve_greedy():
    def solve(N, H, A, B):
        max_a = max(A)
        c = 0
        for b in sorted(B, reverse=True):
            if b <= max_a: break
            c += 1
            H -= b
            if H <= 0: return c
        return c + (H + max_a - 1) // max_a

    N, H = [int(e) for e in input().split()]
    A, B = [], []
    for _ in range(N):
        a, b = [int(e) for e in input().split()]
        A.append(a)
        B.append(b)
    print(solve(N, H, A, B))

class TestClass(unittest.TestCase):
    def atest_sample1(self):
        input = """1 10
3 5"""
        expected = """3"""
        self.assertIO(input, expected)

    def atest_sample2(self):
        input = """2 10
3 5
2 6"""
        expected = """2"""
        self.assertIO(input, expected)

    def atest_sample3(self):
        input = """4 1000000000
1 1
1 10000000
1 30000000
1 99999999"""
        expected = """860000004"""
        self.assertIO(input, expected)

    def test_sample4(self):
        input = """5 500
35 44
28 83
46 62
31 79
40 43"""
        expected = """9"""
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
