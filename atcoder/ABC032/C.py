import sys  # https://docs.python.org/ja/3/library/sys.html


def retsu(N, K, S):
    if 0 in S:
        return N

    left, right, maxlen = 0, 0, 0
    product = 1

    while left < N:
        while right < N and product * S[right] <= K:
            product *= S[right]
            right += 1
        maxlen = max(maxlen, right - left)
        if left < right:
            product //= S[left]
        else:
            right += 1
        left += 1

    return maxlen


def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    S = [int(sys.stdin.readline()) for _ in range(N)]
    print(retsu(N, K, S))


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

    def test_入力例1(self):
        input = """7 6
4
3
1
1
2
10
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """6 10
10
10
10
10
0
10"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """6 9
10
10
10
10
10
10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """4 0
1
2
3
4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
