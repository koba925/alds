def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    A.sort(reverse=True)

    c, l, e = 0, 0, []
    for a in A:
        if a != l:
            l = a
            c = 1
        else:
            c += 1
            if c == 2:
                e.append(l)
                c = 0
                if len(e) == 2:
                    print(e[0] * e[1])
                    break
    else:
        print(0)

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
3 1 2 4 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
3 3 3 3 4 4 4 5 5 5"""
        output = """20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
