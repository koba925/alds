import sys

sys.setrecursionlimit(2000000)

from collections import defaultdict

def sunuke_prime_mine(N, C, services):

    costs = defaultdict(int)
    for i in range(N):
        costs[services[i][0]] += services[i][2] 
        costs[services[i][1] + 1] -= services[i][2]
    
    total = 0
    dates = sorted(costs.keys())
    for i in range(len(dates) - 1):
        costs[dates[i + 1]] += costs[dates[i]]
    for i in range(len(dates) - 1):
        total += min(C, costs[dates[i]]) * (dates[i + 1] - dates[i])

    return total

def sunuke_prime_editorial(N, C, services):
    costs = []
    for s in services:
        costs.append((s[0], s[2]))
        costs.append((s[1] + 1, -s[2]))

    costs.sort()
    
    total = 0
    daily = 0
    prev = 0
    for date, cost in costs:
        if prev != date:
            total += (date - prev) * min(C, daily)
            prev = date
        daily += cost
    
    return total

def resolve():
    N, C = [int(e) for e in sys.stdin.readline().split()]
    services = [[int(e) for e in sys.stdin.readline().split()] for _ in range(N)]
    # print(sunuke_prime_mine(N, C, services))
    print(sunuke_prime_editorial(N, C, services))

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
        input = """2 6
1 2 4
2 2 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1000000000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """163089627821228"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 100000
583563238 820642330 44577
136809000 653199778 90962
54601291 785892285 50554
5797762 453599267 65697
468677897 916692569 87409"""
        output = """88206004785464"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
