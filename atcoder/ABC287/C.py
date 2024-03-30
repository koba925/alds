import sys
from io import StringIO
import unittest

def resolve():
    from collections import defaultdict

    def pathgraph(N, M, G):
        if N != M + 1: return False
        ends = []
        for i, adj in G.items():
            match len(adj):
                case 1: 
                    ends += [i]
                    if len(ends) > 2: return False
                case 2: pass
                case _: return False
        if len(ends) != 2: return False
        visited = set()
        v = ends[0]
        visited.add(v)
        while v != ends[1]:
            if G[v][0] not in visited:
                v = G[v][0]
            elif G[v][1] not in visited:
                v = G[v][1]
            else:
                return False
            visited.add(v)
        return len(visited) == N

    N, M = [int(e) for e in input().split()]
    G = defaultdict(lambda: [])
    for _ in range(M):
        u, v = [int(e) for e in input().split()]
        G[u].append(v)
        G[v].append(u)
    print("Yes" if pathgraph(N, M, G) else "No")

class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """2 1
    1 2"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_my_2(self):
        input = """2 2
    1 2
    2 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_my_3(self):
        input = """2 0"""
        output = """No"""
        self.assertIO(input, output)

    def test_my_4(self):
        input = """2 2
1 1
2 2"""
        output = """No"""
        self.assertIO(input, output)

    def test_sample1(self):
        input = """4 3
1 3
4 2
3 2"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """2 0"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """5 5
1 2
2 3
3 4
4 5
5 1"""
        expected = """No"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
