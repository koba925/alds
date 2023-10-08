def resolve():
    s = input()

    ans = []
    for c in s:
        match c:
            case "0": ans.append("0")
            case "1": ans.append("1")
            case "B": 
                if len(ans) > 0: ans.pop()

    print("".join(ans))

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
        input = """01B0"""
        output = """00"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0BB1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
