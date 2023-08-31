import sys
import collections as cl


def resolve():
    S = sys.stdin.readline().strip()
    Q = int(sys.stdin.readline())

    ans = cl.deque(list(S))
    dir = 1

    for _ in range(Q):
        o, *p = sys.stdin.readline().split()
        if o == "1":
            dir *= -1
        else:
            f, c = p
            if (f == "1" and dir == 1) or (f == "2" and dir == -1):
                ans.appendleft(c)
            else:
                ans.append(c)

    ans = "".join(ans)
    if dir == -1:
        ans = ans[::-1]

    print(ans)


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
        input = """a
4
2 1 p
1
2 2 c
1"""
        output = """cpa"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """a
6
2 2 a
2 1 b
1
2 2 c
1
1"""
        output = """aabc"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """y
1
2 1 x"""
        output = """xy"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
