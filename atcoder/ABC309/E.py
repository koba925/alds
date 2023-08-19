import sys
from collections import defaultdict

def family_and_insurance_naive(N, M, P, ins):
    ins_dict = defaultdict(int)
    for x, y in ins:
        ins_dict[x] = max(ins_dict[x], y)

    ans = 0

    for person in range(1, N + 1):
        generation = 0
        while person:
            if person in ins_dict and ins_dict[person] >= generation:
                ans += 1
                break
            person = P[person]
            generation += 1

    return ans

def family_and_insurance_dp(N, M, P, ins):
    dp = [-1] * (N + 1)
    for x, y in ins:
        dp[x] = max(dp[x], y)

    for person in range(2, N + 1):
        dp[person] = max(dp[person], dp[P[person]] - 1)

    return len([1 for e in dp if e >= 0])

def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    P = [None, 0] + [int(e) for e in sys.stdin.readline().split()]     # 1-based
    ins = [[int(e) for e in sys.stdin.readline().split()] for _ in range(M)]

    # print(family_and_insurance_naive(N, M, P, ins))
    print(family_and_insurance_dp(N, M, P, ins))

# resolve()

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
        input = """7 3
1 2 1 3 3 3
1 1
1 2
4 3"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 10
1 1 3 1 2 3 3 5 7
2 1
5 1
4 3
6 3
2 1
7 3
9 2
1 2
6 2
8 1"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
