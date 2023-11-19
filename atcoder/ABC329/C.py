def resolve():
    import collections as cl
    
    N = input()
    S = input()

    prev, l, length = "", 0, cl.defaultdict(int)
    for s in S:
        if prev == s:
            l += 1
        else:
            l = 1
        length[s] = max(length[s], l)
        prev = s
    print(sum(length.values()))

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
        input = """6
aaabaa"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
x"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12
ssskkyskkkky"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
