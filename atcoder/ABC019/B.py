# TK: ランレングス圧縮、

import sys  # https://docs.python.org/ja/3/library/sys.html


def run_length(seq):
    length = len(seq)
    i, ret = 0, []
    while i < length:
        elem, count = seq[i], 0
        while i + count < length and seq[i + count] == elem:
            count += 1
        ret.append((elem, count))
        i += count
    return ret


def resolve():
    s = sys.stdin.readline().strip()
    print("".join([c + str(l) for c, l in run_length(s)]))


# resolve()
# exit()

import sys
import unittest
from io import StringIO


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例1(self):
        input = """aabbbaad"""
        output = """a2b3a2d1"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """aabbbbbbbbbbbbxyza"""
        output = """a2b12x1y1z1a1"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """edcba"""
        output = """e1d1c1b1a1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
