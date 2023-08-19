import sys

def base_b_to_int(s, b):
    return int(s, b)

def int_to_base_b(n, b):
    if n == 0: return "0"
    d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp = []
    while n > 0:
        temp.append(d[n % b])
        n //= b
    return "".join(reversed(temp))

def base8to9(N, K):
    N2 = N
    for _ in range(K):
        n = base_b_to_int(N, 8)
        N = int_to_base_b(n, 9).replace("8", "5")
    return N

def resolve():
    N, K = sys.stdin.readline().split()
    print(base8to9(N, int(K)))

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
        input = """21 1"""
        output = """15"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1330 1"""
        output = """555"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2311640221315 15"""
        output = """474547"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
