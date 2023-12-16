def resolve_naive_AC():
    K, S = [int(e) for e in input().split()]

    ans = 0
    for x in range(K + 1):
        for y in range(K + 1):
            z = S - x - y
            if 0 <= z <= K: ans += 1
    
    print(ans)

def resolve_O_n():
    K, S = [int(e) for e in input().split()]
    ans = 0
    for x in range(K + 1):
        r = S - x
        if 0 <= r <= 2 * K: ans += min(r, K) - max(0, r - K) + 1
    print(ans)

def resolve_sum():
    K, S = [int(e) for e in input().split()]
    print(sum(S - x - max(0, S - x - K) + 1 for x in range(K + 1) if S - 2 * K <= x <= S))

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
        input = """2 2"""
        output = """6"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 15"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
