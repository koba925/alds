def resolve():
    import sys
    sys.setrecursionlimit(2000000)

    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    def dfs(last, s):
        nonlocal best, bestxs
        if s == N: 
            if last < best:
                best = last
                bestxs = xs[:]
                # debug(xs, s)
            return
        if s > N: return
        for n in range(last + 1, N + 1):
            if s + n > N: return False
            xs.append(n)
            if dfs(n, s + n): return True
            xs.pop()
        return False
    
    N = int(input())
    xs, best, bestxs = [], float("inf"), []
    dfs(0, 0)
    print(*bestxs, sep="\n")

def resolve():
    N = int(input())
    total = 0
    for n in range(1, N + 1):
        total += n
        if total >= N:
            diff = total - N
            break
    for m in range(1, n + 1):
        if m != diff: print(m)
        
    

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
        input = """4"""
        output = """1
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """1
2
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
