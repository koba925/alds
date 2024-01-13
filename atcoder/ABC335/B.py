def resolve():
    N = int(input())

    for x in range(N + 1):
        for y in range(N + 1):
            for z in range(N + 1):
                if x + y + z <= N:
                    print(x, y, z)

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
        input = """3"""
        output = """0 0 0
0 0 1
0 0 2
0 0 3
0 1 0
0 1 1
0 1 2
0 2 0
0 2 1
0 3 0
1 0 0
1 0 1
1 0 2
1 1 0
1 1 1
1 2 0
2 0 0
2 0 1
2 1 0
3 0 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4"""
        output = """0 0 0
0 0 1
0 0 2
0 0 3
0 0 4
0 1 0
0 1 1
0 1 2
0 1 3
0 2 0
0 2 1
0 2 2
0 3 0
0 3 1
0 4 0
1 0 0
1 0 1
1 0 2
1 0 3
1 1 0
1 1 1
1 1 2
1 2 0
1 2 1
1 3 0
2 0 0
2 0 1
2 0 2
2 1 0
2 1 1
2 2 0
3 0 0
3 0 1
3 1 0
4 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
