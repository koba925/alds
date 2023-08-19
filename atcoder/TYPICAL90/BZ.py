import sys

def easy_graph_problem(n, _, adjs):
    ans = 0
    for i in range(1, n + 1):
        c = 0
        for a in adjs[i]:
            if a < i:
                c += 1
        if c == 1:
            ans += 1
    return ans
 
def easy_graph_problem_functional(n, _, adjs):
    return len([
        i for i in range(1, n + 1) 
        if len([i for a in adjs[i] if a < i]) == 1
    ])

def resolve():
    N, M = [int(e) for e in sys.stdin.readline().split()]
    adjs = [None] + [[] for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()]
        adjs[a].append(b)
        adjs[b].append(a)

    print(easy_graph_problem(N, M, adjs))

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
        input = """5 5
1 2
1 3
3 2
5 2
4 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1
1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 18
7 2
1 6
5 2
1 3
7 6
5 3
5 6
5 4
1 7
2 6
3 4
5 1
4 7
4 6
5 7
3 2
4 2
1 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
