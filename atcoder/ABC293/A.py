def resolve():
    S = input()
    ans = []
    for i in range(len(S) // 2):
        ans += S[2 * i + 1] + S[2 * i]
    print("".join(ans))

def resolve():
    S = input()
    print("".join(b + a for a, b in zip(S[::2], S[1::2])))

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
        input = """abcdef"""
        output = """badcfe"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaaa"""
        output = """aaaa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """atcoderbeginnercontest"""
        output = """taocedbrgeniencrnoetts"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
