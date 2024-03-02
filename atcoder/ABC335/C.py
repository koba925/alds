def resolve():
    N , Q = [int(e) for e in input().split()]
    D: list[tuple[int, int]] = [(i, 0) for i in range(1, N + 1)]

    head = 0
    dx = {"R": 1, "L": -1, "U": 0, "D": 0}
    dy = {"R": 0, "L": 0, "U": 1, "D": -1}
    
    for _ in range(Q):
        c, p = input().split()
        match c:
            case "1":
                cur = D[head]
                head = (head - 1) % N
                D[head] = (cur[0] + dx[p], cur[1] + dy[p])
            case "2":
                print(*D[(head + int(p) - 1) % N])

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
        input = """5 9
2 3
1 U
2 3
1 R
1 D
2 3
1 L
2 1
2 5"""
        output = """3 0
2 0
1 1
1 0
1 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
