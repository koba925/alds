import sys

def vacation(N, D, S):
    def all_holiday(d):
        return all(sched[d] == "o" for sched in S)

    days = max_days = 0
    for d in range(D):
        if all_holiday(d):
            days += 1
            max_days = max(max_days, days)
        else:
            days = 0
    return max_days

def resolve():
    N, D = [int(e) for e in sys.stdin.readline().split()]
    S = [sys.stdin.readline().strip() for _ in range(N)]
    print(vacation(N, D, S))

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
        input = """3 5
xooox
oooxx
oooxo"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
oxo
oxo
oxo"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3
oox
oxo
xoo"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 7
ooooooo"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """5 15
oxooooooooooooo
oxooxooooooooox
oxoooooooooooox
oxxxooooooxooox
oxooooooooxooox"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
