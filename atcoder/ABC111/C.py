def resolve():
    import collections as cl

    N = int(input())
    V = [int(e) for e in input().split()]

    evens, odds = V[0::2], V[1::2]
    count_evens = cl.Counter(evens)
    count_odds = cl.Counter(odds)
    sorted_evens = count_evens.most_common()
    sorted_odds = count_odds.most_common()

    if sorted_evens[0][0] != sorted_odds[0][0]:
        print(N // 2 - sorted_evens[0][1] + N // 2 - sorted_odds[0][1])
    else:
        stay_evens = sorted_evens[1][1] if len(sorted_evens) > 1 else 0
        stay_odds = sorted_odds[1][1] if len(sorted_odds) > 1 else 0 
        if stay_evens < stay_odds:
            print(N // 2 - sorted_evens[0][1] + N // 2 - stay_odds)
        else:
            print(N // 2 - stay_evens + N // 2 - sorted_odds[0][1])

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

    def test_1(self):
        input = """8
1 1 1 1 2 3 2 3"""
        output = """4"""
        self.assertIO(input, output)
    
    def test_2(self):
        input = """10
1 1 1 1 1 1 2 2 2 3"""
        output = """5"""
        self.assertIO(input, output)


    def test_入力例_1(self):
        input = """4
3 1 3 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
105 119 105 119 105 119"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 1 1 1"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
