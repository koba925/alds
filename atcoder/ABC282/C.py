def resolve():
    def solve(N, S):
        ret = []
        outside = True
        for s in S:
            if s == "\"": outside = not outside
            if outside and s == ",": s = "."
            ret.append(s)
        return "".join(ret)
    
    N = int(input())
    S = input()
    print(solve(N, S))

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
        input = """8
"a,b"c,d"""
        output = """"a,b"c.d"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
,,,,,"""
        output = """....."""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
a,"t,"c,"o,"d,"e,"r,"""
        output = """a."t,"c."o,"d."e,"r."""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
