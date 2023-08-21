# LL: 面倒な条件は整理して確実に

import sys  # https://docs.python.org/ja/3/library/sys.html


def accepted(S):
    count = 0

    for i, c in enumerate(S):
        if i == 0:
            if c != "A":
                return False
        elif 2 <= i < len(S) - 1 and c == "C":
            count += 1
        elif not c.islower():
            return False

    return count == 1


def resolve():
    S = sys.stdin.readline().strip()
    print("AC" if accepted(S) else "WA")


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
        input = """AtCoder"""
        output = """AC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ACoder"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """AcycliC"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """AtCoCo"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """Atcoder"""
        output = """WA"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
