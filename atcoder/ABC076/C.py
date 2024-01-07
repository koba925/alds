def resolve():
    def match(s, t):
        for c, d in zip(s, t):
            if c == "?": continue
            if c != d: return False
        return True
    
    S, T = input(), input()

    ls, lt = len(S), len(T)
    max_str = "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"
    ans = max_str
    for i in range(ls - lt + 1):
        if match(S[i: i + lt], T):
            s = S[:i] + T + S[i + lt:]
            s = s.replace("?", "a")
            ans = min(ans, s)

    print("UNRESTORABLE" if ans == max_str else ans)

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
        input = """?tc????
coder"""
        output = """atcoder"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """??p??d??
abc"""
        output = """UNRESTORABLE"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
