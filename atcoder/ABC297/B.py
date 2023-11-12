def resolve():
    import collections as cl

    S = input()
    D = cl.defaultdict(list)
    for i, s in enumerate(S):
        D[s].append(i)
    parity = D["B"][0] % 2 != D["B"][1] % 2
    kinr = D["R"][0] < D["K"][0] < D["R"][1]
    print("Yes" if parity and kinr else "No")


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
        input = """RNBQKBNR"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """KRRBBNNQ"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """BRKRBQNN"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
