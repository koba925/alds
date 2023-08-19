import sys

from math import pi, degrees, sin, cos, atan2

def statue(T, L, X, Y, e):
    k_rad = 2 * pi * e / T
    k_y = -L / 2 * sin(k_rad)
    k_z = L / 2 - L / 2 * cos(k_rad)
    diff_x = X - 0
    diff_y = Y - k_y
    diff_z = k_z - 0
    dist = (diff_x ** 2 + diff_y ** 2) ** 0.5
    theta = atan2(diff_z, dist)
    return degrees(theta)

def resolve():
    T = int(sys.stdin.readline())
    L, X, Y = [int(e) for e in sys.stdin.readline().split()]
    Q = int(sys.stdin.readline())
    for _ in range(Q):
        e = int(sys.stdin.readline())
        print(f"{statue(T, L, X, Y, e):0.12f}")

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
        input = """4
2 1 1
4
0
1
2
3"""
        output = """0.000000000000
24.094842552111
54.735610317245
45.000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5121
312000000 4123 3314
6
123
12
445
4114
42
1233"""
        output = """4.322765775902
0.421184234768
15.640867693969
35.396039162484
1.475665637902
43.338582976959"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
