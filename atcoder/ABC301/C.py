def resolve():
    import collections as cl

    def solve(S, T):
        CS, CT = cl.Counter(S), cl.Counter(T)
        for c in "bfghijklmnpqsuvwxyz":
            if CS[c] != CT[c]: return False
        sdiff, tdiff = 0, 0
        for c in "atcoder":
            if CS[c] > CT[c]:
                sdiff += CS[c] - CT[c]
            elif CS[c] < CT[c]:
                tdiff += CT[c] - CS[c]
        return sdiff <= CT["@"] and tdiff <= CS["@"]
    
    S, T = input(), input()
    print("Yes" if solve(S, T) else "No")

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
        input = """ch@ku@ai
choku@@i"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ch@kud@i
akidu@ho"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """aoki
@ok@"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """aa
bb"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
