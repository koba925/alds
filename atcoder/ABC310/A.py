import sys

def resolve():
    N, P, Q = [int(e) for e in sys.stdin.readline().split()]
    D = [int(e) for e in sys.stdin.readline().split()]    
    print(min(P, Q + min(D)))

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
        input = """3 100 50
60 20 40"""
        output = """70"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 100 50
60000 20000 40000"""
        output = """100"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
