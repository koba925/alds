import sys


def resolve():
    O = input()
    E = input()

    for i in range(len(O)):
        print(O[i], end="")
        if i < len(E):
            print(E[i], end="")
    print()


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
        input = """xyz
abc"""
        output = """xaybzc"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """atcoderbeginnercontest
atcoderregularcontest"""
        output = """aattccooddeerrbreeggiunlnaerrccoonntteesstt"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
