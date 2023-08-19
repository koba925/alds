import sys

def resolve():
    S = sys.stdin.readline().strip()
    # print("yes" if len(S) == len(set(S)) else "no")

    # used = set()
    # for s in S:
    #     if s in used:
    #         print("no")
    #         break
    #     used.add(s)
    # else:
    #     print("yes")

    ok = True
    for i in range(1, len(S)):
        for j in range(0, i):
            if S[i] == S[j]:
                ok = False
                break
        if not ok:
            break
    print("yes" if ok else "no")
    
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
        input = """uncopyrightable"""
        output = """yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """different"""
        output = """no"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """no"""
        output = """yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
