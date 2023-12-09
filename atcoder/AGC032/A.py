def resolve_tle():
    def debug(*args, **kwargs): print(*args, **kwargs, file=sys.stderr)

    import sys
    import collections as cl

    sys.setrecursionlimit(1000)
    
    def search(l, A, C, ops):
        if l == N:
            return ops if A == B else False

        for j in C.keys():
            if j > l + 1 or C[j] == 0: continue
            C[j] -= 1
            result = search(l + 1, A[:j - 1] + [j] + A[j - 1:], C, ops + [j])
            if result: return result
            C[j] += 1

        return False

    N = int(input())
    B = [int(e) for e in input().split()]
    C = cl.Counter(B)

    ops = search(0, [], C, [])
    print(*ops if ops else [-1], sep="\n")

def resolve():
    N = int(input())
    B = [int(e) for e in input().split()]

    ans = []
    for i in range(N):
        for k in reversed(range(len(B))):
            if B[k] == k + 1:
                ans.append(k + 1)
                del B[k]
                break
    if B:
        print(-1)
    else:
        print(*ans[::-1], sep="\n")

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
1 2 1"""
        output = """1
1
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
2 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9
1 1 1 2 2 1 2 3 2"""
        output = """1
2
2
3
1
2
2
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
