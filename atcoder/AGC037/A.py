def resolve():
    S = input()
    K = 1
    prev_str = S[0]
    cur_str = ""
    for c in S[1:]:
        cur_str += c
        if prev_str != cur_str:
            K += 1
            prev_str = cur_str
            cur_str = ""
    print(K)


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
        input = """a"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """aabbaa"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaaccacabaababc"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
