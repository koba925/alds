import sys  # https://docs.python.org/ja/3/library/sys.html

sys.setrecursionlimit(2000000)


def roulettes(N, M, CPS):
    point, money = 0, 0
    while True:
        rest = M - point
        E = [
            (sum([min(s, rest) for s in cps[2]]) / cps[0] / cps[1], i)
            for i, cps in enumerate(CPS)
        ]
        _, best_i = max(E)
        plus_point = sum(CPS[best_i][2]) / CPS[best_i][1]
        plus_point = sum([min(s, rest) for s in CPS[best_i][2]]) / CPS[best_i][1]
        plus_money = CPS[best_i][0]
        if point + plus_point >= M:
            break
        point += plus_point
        money += plus_money

    money += plus_money * plus_point / rest
    return money


def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    CPS = []
    for _ in range(N):
        c, p, *s = [int(e) for e in sys.stdin.readline().split()]
        CPS.append((c, p, s))
    print(roulettes(N, M, CPS))


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
        input = """3 14
100 2 5 9
50 4 1 2 4 8
70 5 2 4 2 8 8"""
        output = """215.913355350494384765625"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 100
1 2 1 2
10 6 0 0 0 0 0 100"""
        output = """60"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20 90
3252 9 0 4 2 7 3 2 3 2 4
2147 1 1
4033 8 0 4 1 7 5 2 5 0
3795 6 6 6 2 3 2 2
3941 7 2 4 4 7 2 0 5
2815 6 2 1 0 5 2 2
3020 2 3 6
3858 9 4 2 7 3 0 4 4 6 5
4533 10 3 6 4 0 6 4 4 2 7 7
4198 8 6 7 0 6 3 6 5 6
3739 8 2 7 1 5 1 4 4 7
2465 4 1 4 0 1
4418 9 7 6 2 4 6 1 5 0 7
5450 12 0 4 4 7 7 4 4 5 4 5 3 7
4196 9 1 6 5 5 7 2 3 6 3
4776 9 2 2 7 3 6 6 1 6 6
2286 3 3 5 6
3152 3 4 1 5
3509 7 0 6 7 0 1 0 3
2913 6 0 1 5 0 5 6"""
        output = """45037.072314895291126319493887599716"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
