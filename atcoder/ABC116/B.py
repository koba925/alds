import sys

from itertools import count

def collatz_problem(S):
    collatz = {S}
    for i in count(2):
        S = S // 2 if S % 2 == 0 else 3 * S + 1
        if S in collatz:
            return i
        collatz.add(S)

def resolve():
    S = int(sys.stdin.readline())

    print(collatz_problem(S))

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
        input = """8"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7"""
        output = """18"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """54"""
        output = """114"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
