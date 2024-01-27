def resolve():
    print(input().translate(str.maketrans({"0": "1", "1": "0"})))

def resolve():
    print("".join("1" if c == "0" else "0" for c in input()))

def resolve():
    print("".join(map(lambda c: "1" if c == "0" else "0", input())))
    

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
        input = """01"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1011"""
        output = """0100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100100001"""
        output = """011011110"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
