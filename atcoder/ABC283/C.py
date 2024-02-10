def resolve():
    print(len(input().replace("00", "0")))

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
        input = """40004"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1355506027"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10888869450418352160768000001"""
        output = """27"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
