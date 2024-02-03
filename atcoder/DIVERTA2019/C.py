def resolve():
    N = int(input())
    S = [input() for _ in range(N)]

    ab = lasta = firstb = lasta_firstb = 0 
    for s in S:
        ab += s.count("AB")
        if s[-1] == "A": lasta += 1
        if s[0] == "B": firstb += 1
        if s[-1] == "A" and s[0] == "B": lasta_firstb += 1
    if lasta == 0 or firstb == 0:
        print(ab)
    elif lasta > firstb:
        print(ab + firstb)
    elif lasta < firstb:
        print(ab + lasta)
    elif lasta == lasta_firstb:
        print(ab + lasta - 1)
    else:
        print(ab + lasta) 


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

    def test_my_1(self):
        input = """3
BA
BA
CC"""
        output = """1"""
        self.assertIO(input, output)

    def test_my_2(self):
        input = """1
BA
"""
        output = """0"""
        self.assertIO(input, output)

    def test_my_3(self):
        input = """1
AB
"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """3
ABCA
XBAZ
BAD"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
BEWPVCRWH
ZZNQYIJX
BAVREA
PA
HJMYITEOX
BCJHMRMNK
BP
QVFABZ
PRGKSPUNA"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
RABYBBE
JOZ
BMHQUVA
BPA
ISU
MCMABAOBHZ
SZMEHMA"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
