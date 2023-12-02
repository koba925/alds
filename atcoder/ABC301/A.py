def resolve_1():
    N, S = int(input()), input()
    twin, awin = S.count("T"), S.count("A")
    print("T" if twin > awin else "A" if awin > twin else "T" if S[-1] == "A" else "A")

def resolve():
    N, S = int(input()), input()
    twin = awin = 0
    for i in range(N):
        if S[i] == "T":
            twin += 1
            ti = i
        else:
            awin += 1
            ai = i    
    print("T" if twin > awin else "A" if awin > twin else "T" if ti < ai else "A")

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

    def test_01_random_09(self):
        input = """90
ATTTTATATATTATTAATATATTAATTATTAAATTAAATTATTTATTAATAAAAATATTATTTTAATAAAAATTAAAAAAAATATTTTTT"""
        output = """A"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """5
TTAAT"""
        output = """T"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
ATTATA"""
        output = """T"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
A"""
        output = """A"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
