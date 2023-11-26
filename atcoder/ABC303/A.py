def resolve_mine():
    similar = lambda x, y: (
        x == y or 
        (x == "1" and y == "l") or (x == "l" and y == "1") or
        (x == "0" and y == "o") or (x == "o" and y == "0"))
    
    N, S, T = int(input()), input(), input()
    print("Yes" if all(similar(x, y) for x, y in zip(S, T)) else "No")
        
def resolve():
    N = int(input())
    S = input().replace("0", "o").replace("1", "l")
    T = input().replace("0", "o").replace("1", "l")
    print("Yes" if S == T else "No")

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
        input = """3
l0w
1ow"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
abc
arc"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
nok00
n0koo"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
