def resolve():
    S = input()
    i = 0
    while i < len(S) and S[i] == "A":
        i += 1
    while i < len(S) and S[i] == "B":
        i += 1
    while i < len(S) and S[i] == "C":
        i += 1
    print("Yes" if i == len(S) else "No")

def resolve():
    def abc(S):
        l = len(S)
        for a in range(l + 1):
            A = "A" * a
            for b in range(l - a + 1):
                ABC = A + "B" * b + "C" * (l - a - b)
                if ABC == S: return True
        return False
        
    S = input()
    print("Yes" if abc(S) else "No")                


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
        input = """AAABBBCCCCCCC"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ACABABCBC"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """A"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """ABBBBBBBBBBBBBCCCCCC"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
