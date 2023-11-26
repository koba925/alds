def resolve_at_contest():
    D = int(input())
    m, l, r = D, 0, int(D ** 0.5 + 0.5)
    while l <= r:
        v = l * l + r * r - D
        m = min(m, abs(v))
        if v < 0: l += 1
        elif v > 0: r -= 1
        else: break
    print(m)

def resolve():
    D = int(input())

    ans = D
    xmax = int(D ** 0.5 + 0.5)
    for x in range(0, xmax + 1):
        C = x * x - D
        if C >= 0:
            ans = min(ans, C)
        else:
            y = int((-C) ** 0.5 - 0.5)
            ans = min(ans, abs(C + y * y))
            y += 1
            ans = min(ans, abs(C + y * y))

    print(ans)

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
        input = """36"""
        output = """0"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """21"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """998244353"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """264428617"""
        output = """32"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
