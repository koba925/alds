def resolve():
    N, Q = [int(e) for e in input().split()]
    yel = [0] * N
    red = [0] * N
    for _ in range(Q):
        c, x = [int(e) for e in input().split()]
        x -= 1
        match c:
            case 1: yel[x] += 1
            case 2: red[x] += 1
            case 3: print("Yes" if yel[x] >= 2 or red[x] >= 1 else "No")

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
        input = """3 9
3 1
3 2
1 2
2 1
3 1
3 2
1 2
3 2
3 3"""
        output = """No
No
Yes
No
Yes
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
