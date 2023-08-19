import sys

sys.setrecursionlimit(2000000)

def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)

def atcoder_mine(S):
    l, ans = 0, 0
    for c in S:
        if c in "ACGT":
            l += 1
            ans = max(ans, l)
        else:
            l = 0
    return ans

def atcoder_editorial(S):
    ans = 0
    for left in range(0, len(S)):
        for right in range(left + 1, len(S) + 1):
            # debug(S[left:right])
            if all([c in "ACGT" for c in S[left:right]]):
                ans = max(ans, right - left)
    return ans

def resolve():
    S = input()

    # print(atcoder_mine(S))
    print(atcoder_editorial(S))

# resolve()

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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """HATAGAYA"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """SHINJUKU"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
