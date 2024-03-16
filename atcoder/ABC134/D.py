import sys
from io import StringIO
import unittest

def resolve_TLE():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    def answer(k):
        ans = [i for i, b in enumerate(f"{k:0{N}b}"[::-1], 1) if b == "1"]
        print(len(ans))
        if ans: print(*ans)
 
    N = int(input())
    A = [0] + [int(e) for e in input().split()]

    for k in range(2 ** N):
        choice = [0] + [int(b) for b in f"{k:0{N}b}"[::-1]]
        debug(choice)
        for i in range(1, N + 1):
            debug(i, A[i], [c for c in choice[i::i]])
            if A[i] != sum(c for c in choice[i::i]) % 2:
                debug("NG")
                break
        else:
            answer(k)
            break

def resolve():
    N = int(input())
    A = [0] + [int(e) for e in input().split()]

    B = [-1] * (N + 1)
    for i in range(N, 0, -1):
        s = 0
        for j in range(2 * i, N + 1, i):
            s += B[j]
        B[i] = 0 if A[i] == s % 2 else 1

    ans = [i for i in range(1, N + 1) if B[i] == 1]
    print(len(ans))
    if ans: print(*ans)

class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """6
1 0 1 0 0 1"""
        output = """3
1 2 6"""
        self.assertIO(input, output)
    
    def test_sample1(self):
        input = """3
1 0 0"""
        expected = """1
1"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5
0 0 0 0 0"""
        expected = """0"""
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
