# TK: str.translate str.maketrans

def resolve():
    N, S = int(input()), input()
    Q = int(input())

    s = "abcdefghijklmnopqrstuvwxyz"
    t = "abcdefghijklmnopqrstuvwxyz"

    for _ in range(Q):
        c, d = input().split()
        t = t.replace(c, d)

    print(S.translate(str.maketrans(s, t)))

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
        input = """7
atcoder
4
r a
t e
d v
a r"""
        output = """recover"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
abc
4
a a
s k
n n
z b"""
        output = """abc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """34
supercalifragilisticexpialidocious
20
g c
l g
g m
c m
r o
s e
a a
o f
f s
e t
t l
d v
p k
v h
x i
h n
n j
i r
s i
u a"""
        output = """laklimamriiamrmrllrmlrkramrjimrial"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
