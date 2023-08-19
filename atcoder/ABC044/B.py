import sys
from collections import Counter


def beautiful(w):
    c = Counter(w)
    return all(v % 2 == 0 for v in c.values())


def resolve():
    w = sys.stdin.readline().strip()
    print("Yes" if beautiful(w) else "No")


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
        input = """abaccaba"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hthth"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
