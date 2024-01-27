def resolve():
    N = int(input())
    S = input()

    LRUD = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D":(0, -1)}
    x, y, visited = 0, 0, set()
    visited.add((x, y))
    for s in S:
        x += LRUD[s][0]
        y += LRUD[s][1]
        if (x, y) in visited:
            print("Yes")
            break
        visited.add((x, y))
    else:
        print("No")

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
        input = """5
RLURU"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20
URDDLLUUURRRDDDDLLLL"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
