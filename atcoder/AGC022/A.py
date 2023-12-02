def resolve():
    import string
    import collections as cl

    S = list(input())
    if len(S) == 26:
        letters = set([S[25]])
        del S[25]
        for i in reversed(range(25)):
            if S[i] < max(letters):
                S[i] = min(l for l in letters if l > S[i])
                print("".join(S))
                break
            letters.add(S[i])
            del S[i]
        else:
            print(-1)
    else:
        letters = set(S)
        for a in string.ascii_lowercase:
            if a not in letters:
                print("".join(S + [a]))
                break



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
        input = """atcoder"""
        output = """atcoderb"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abc"""
        output = """abcd"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """zyxwvutsrqponmlkjihgfedcba"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """abcdefghijklmnopqrstuvwzyx"""
        output = """abcdefghijklmnopqrstuvx"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
