def can_match(s, t):
    if s == t:
        return True
    if len(s) == len(t):
        cnt = 0
        for si, ti in zip(s, t):
            if si != ti:
                cnt += 1
                if cnt >= 2:
                    return False
        return True
    
    if len(s) == len(t) + 1:
        si, ti, cnt = 0, 0, 0
        while si < len(s) and ti < len(t):
            if s[si] != t[ti]:
                si += 1
                cnt += 1
                if cnt >= 2:
                    return False
                continue
            si += 1
            ti += 1
        return ((si == len(s) - 1 and cnt == 0) or (si == len(s) and cnt == 1)) and ti == len(t)
    
    if len(s) == len(t) - 1:
        si, ti, cnt = 0, 0, 0
        while si < len(s) and ti < len(t):
            if s[si] != t[ti]:
                ti += 1
                cnt += 1
                if cnt >= 2:
                    return False
                continue
            si += 1
            ti += 1
        return si == len(s) and ((ti == len(t) - 1 and cnt == 0) or (ti == len(t) and cnt == 1)) 

    return False

def error_correction_first(N, T, S):
    ans = []
    for i, s in enumerate(S, 1):
        if can_match(s, T):
            ans.append(i)
    return ans

def match_to(s, t):
    for i, c in enumerate(s, 0):
        if len(t) <= i or c != t[i]:
            return i
    return i + 1
        
def error_correction(N, T, S):
    ans = []
    TR = T[::-1]
    for i, s in enumerate(S, 1):
        left = match_to(s, T)
        right = match_to(s[::-1], TR)
        if len(s) == len(T):
            if left == right == len(s):
                ans += [i]
            elif left + right == len(s) -1:
                ans += [i]
        elif len(s) == len(T) - 1 and left + right >= len(s):
            ans += [i]
        elif len(s) == len(T) + 1 and left + right >= len(T):
            ans += [i]
    return ans

def resolve():
    N, T = input().split()
    N = int(N)
    S = [input() for _ in range(N)]

    ans = error_correction(N, T, S)
    print(len(ans))
    print(*ans)

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
        input = """1 atcoder
atcode"""
        output = """1
1"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """5 ababc
ababc
babc
abacbc
abdbc
abbac"""
        output = """4
1 2 3 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 aoki
takahashi"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 atcoder
atoder
atcode
athqcoder
atcoder
tacoder
jttcoder
atoder
atceoder
atcoer"""
        output = """6
1 2 4 7 8 9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
