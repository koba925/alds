import sys

def keyence(S):
    if S == "keyence":
        return True
    
    N = len(S)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if S[:i] + S[j:] == "keyence":
                return True
    return False

def resolve():
    S = sys.stdin.readline().strip()    
    print("YES" if keyence(S) else "NO")

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
        input = """keyofscience"""
        output = """YES"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """mpyszsbznf"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """ashlfyha"""
        output = """NO"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """keyence"""
        output = """YES"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
