def resolve():
    import collections as cl

    S = input()
    C = cl.Counter(S)
    most = C.most_common(1)[0][1]
    for k, v in sorted(C.items()):
        if v == most:
            print(k)
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
        input = """frequency"""
        output = """e"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoder"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """pseudopseudohypoparathyroidism"""
        output = """o"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
