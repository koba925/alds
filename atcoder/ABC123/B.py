import sys

def resolve_nlogn():
    deliveries = []
    for _ in range(5):
        t = int(sys.stdin.readline())
        deliveries.append((10 if t % 10 == 0 else t % 10, t, (t + 9) // 10 * 10))
    deliveries.sort()    
    print(deliveries[0][1] + sum(d[2] for d in deliveries[1:]))

from itertools import permutations

def resolve_exhaustive():
    def delivery_time(p):
        return sum((t + 9) // 10 * 10 for t in p[:4]) + p[4]
    
    T = [int(sys.stdin.readline()) for _ in range(5)]
    print(min(delivery_time(p) for p in permutations(T)))

def resolve():
    resolve_exhaustive()


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
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
