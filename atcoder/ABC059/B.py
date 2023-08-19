import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve_easy():
    A = int(sys.stdin.readline())
    B = int(sys.stdin.readline())
    print("GREATER" if A > B else "LESS" if A < B else "EQUAL")


def resolve():
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    la, lb = len(A), len(B)
    if la > lb:
        print("GREATER")
    elif la < lb:
        print("LESS")
    else:
        for a, b in zip(A, B):
            if a > b:
                print("GREATER")
                break
            elif a < b:
                print("LESS")
                break
        else:
            print("EQUAL")


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
        input = """36
24"""
        output = """GREATER"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """850
3777"""
        output = """LESS"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9720246
22516266"""
        output = """LESS"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """123456789012345678901234567890
234567890123456789012345678901"""
        output = """LESS"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
