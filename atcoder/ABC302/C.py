def resolve():
    import itertools as it

    def solve(N, M, S):
        for ps in it.permutations(S):
            for a, b in it.pairwise(ps):
                if len([1 for ca, cb in zip(a, b) if ca != cb]) >= 2:
                    break
            else:
                return True
        return False
    
    N, M = [int(e) for e in input().split()]
    S = [input() for _ in range(N)]
    print("Yes" if solve(N, M, S) else "No")

def resolve():
    import itertools

    # 文字列 A, B の文字が異なる箇所の個数を求める関数
    def diff(A, B):
        res = 0
        for a, b in zip(A, B):
            if a != b:
                res += 1
        return res

    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    S.sort()

    for T in itertools.permutations(S):
        ok = True
        for t1, t2 in itertools.pairwise(T):
            if diff(t1, t2) != 1:
                ok = False
        if ok:
            print("Yes")
            return
    print("No")

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
        input = """4 4
bbed
abcd
abed
fbed"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5
abcde
abced"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 4
fast
face
cast
race
fact
rice
nice
case"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
