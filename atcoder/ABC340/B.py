def resolve():
    Q = int(input())

    A = []
    for _ in range(Q):
        c, d = [int(e) for e in input().split()]
        if c == 1:
            A.append(d)
        else:
            print(A[-d])



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
1 20
1 30
2 1
1 40
2 3"""
        output = """30
20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
