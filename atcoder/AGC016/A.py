def resolve():
    s = input()
    min_cnt = float("inf")

    for c in set(s):
        cnt, S = 0, list(s)
        while not all([C == c for C in S]):
            for i in range(len(S) - 1):
                if S[i + 1] == c:
                    S[i] = c
            S.pop()
            cnt += 1
        min_cnt = min(min_cnt, cnt)    

    print(min_cnt)

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
        input = """serval"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """jackal"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """zzz"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """whbrjpjyhsrywlqjxdbrbaomnw"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
