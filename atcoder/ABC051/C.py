def resolve():
    sx, sy, tx, ty = [int(e) for e in input().split()]
    w, h = tx - sx, ty - sy
    
    go1 = "U" * h + "R" * w
    back1 = "D" * h + "L" * w
    go2 = "L" + "U" * (h + 1) + "R" * (w + 1) + "D"
    back2 = "R" + "D" * (h + 1) + "L" * (w + 1) + "U"

    print(go1 + back1 + go2 + back2)

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
        input = """0 0 1 2"""
        output = """UURDDLLUUURRDRDDDLLU"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-2 -2 1 1"""
        output = """UURRURRDDDLLDLLULUUURRURRDDDLLDL"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
