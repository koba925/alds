def resolve_contest():
    S = input()
    if S[0] == S[1]:
        c = S.replace(S[0], "")
    elif S[0] == S[2]:
        c = S[1]
    else:
        c = S[0]
    print(S.find(c) + 1)

def resolve_2path():
    import collections as cl
    S = input()
    for k, v in cl.Counter(S).items():
        if v == 1: c = k
    print(S.find(c) + 1)

def resolve():
    S = input()
    c = S[0] if S[0] == S[1] else S[2]
    print(next(i for i, s in enumerate(S, 1) if s != c))

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
        input = """yay"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """egg"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """zzzzzwz"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
