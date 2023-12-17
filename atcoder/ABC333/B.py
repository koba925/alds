def resolve():
    nbr = {"A": ("E", "B"), "B": ("A", "C"), "C": ("B", "D"), "D": ("C", "E"), "E": ("D", "A")}

    S, T = input(), input()
    snbr = S[1] in nbr[S[0]]
    tnbr = T[1] in nbr[T[0]]
    print("Yes" if snbr == tnbr else "No")

def resolve():
    nbr = "ABCDEAEDCBA"

    S, T = input(), input()
    snbr = S in nbr
    tnbr = T in nbr
    print("Yes" if snbr == tnbr else "No")


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
        input = """AB
EA"""
        output = """Yes"""
        self.assertIO(input, output)
    
    def test_2(self):
        input = """BD
EC"""
        output = """Yes"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """AC
EC"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """DA
EA"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """BD
BD"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
