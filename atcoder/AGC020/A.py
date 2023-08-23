import sys  # https://docs.python.org/ja/3/library/sys.html


def resolve():
    N, A, B = [int(e) for e in sys.stdin.readline().split()]
    print("Alice" if (B - A) % 2 == 0 else "Borys")


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
        input = """5 2 4"""
        output = """Alice"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1 2"""
        output = """Borys"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """58 23 42"""
        output = """Borys"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
