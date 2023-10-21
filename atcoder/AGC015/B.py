def resolve():
    def from_floor(floor, direction):
        if direction == "U":
            return 2 * (floor - 1) + 1 * (N - floor) 
        else:
            return 1 * (floor - 1) + 2 * (N - floor) 
    
    S = input()
    N = len(S)

    print(sum(from_floor(floor, direction) for floor, direction in enumerate(S, 1)))

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
        input = """UUD"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """UUDUUDUD"""
        output = """77"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
