import sys

def medicine(N, K, M):
    total = sum([m[1] for m in M])
    if total <= K:
        return 1 
    for day, num in M:
        total -= num
        if total <= K:
            return day + 1

def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    M = [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    M.sort()
    print(medicine(N, K, M))

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
        input = """4 8
6 3
2 5
1 9
4 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 100
6 3
2 5
1 9
4 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 158260522
877914575 2436426
24979445 61648772
623690081 33933447
476190629 62703497
211047202 71407775
628894325 31963982
822804784 50968417
430302156 82631932
161735902 80895728
923078537 7723857
189330739 10286918
802329211 4539679
303238506 17063340
492686568 73361868
125660016 50287940"""
        output = """492686569"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
