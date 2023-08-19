import sys

from itertools import count

def is_prime(n):
    for k in range(2, int(n ** 0.5)):
        if n % k == 0:
            return False
    return True

def next_prime(x):
    return (n for n in count(x) if is_prime(n)).__next__()

def resolve():
    X = int(sys.stdin.readline())
    print(next_prime(X))

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
        input = """20"""
        output = """23"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """99992"""
        output = """100003"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
