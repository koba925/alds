def resolve():
    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]

    votes = [0] * N
    top_vote, top_voter = 0, 0

    for a in A:
        a -= 1
        votes[a] += 1
        if votes[a] > top_vote:
            top_voter = a
            top_vote = votes[a]
        elif votes[a] == top_vote:
            if a < top_voter:
                top_voter = a
        print(top_voter + 1)

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
        input = """3 7
1 2 2 3 1 3 3"""
        output = """1
1
2
2
1
1
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100 5
100 90 80 70 60"""
        output = """100
90
80
70
60"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """9 8
8 8 2 2 8 8 2 2"""
        output = """8
8
8
2
8
8
8
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
