import sys
from io import StringIO
import unittest

def resolve():
    def unicyclic(N, M, G):
        def dfs(i, group):
            groups[i] = group
            to_go = [i]
            while to_go:
                i = to_go.pop()
                for j in G[i]:
                    if groups[j] == -1:
                        groups[j] = group
                        to_go.append(j)
        
        groups = [-1] * N
        group = 0
        for i in range(N):
            if groups[i] != -1:
                continue
            dfs(i, group)
            group += 1

        vertexes, edges = [0] * group, [0] * group
        for i, g in enumerate(groups):
            vertexes[g] += 1
            edges[g] += len(G[i])
        
        for i in range(group):
            if vertexes[i] * 2 != edges[i]:
                return False
        return True
        
    N, M = [int(e) for e in input().split()]
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v = [int(e) for e in input().split()]
        G[u - 1].append(v - 1)
        G[v - 1].append(u - 1)
    print("Yes" if unicyclic(N, M, G) else "No")

# resolve()
# exit()

class TestClass(unittest.TestCase):
    def test_my_(self):
        input = """2 3
1 1
1 1
2 2"""
        output = """No"""
        self.assertIO(input, output)
    
    def test_sample1(self):
        input = """3 3
2 3
1 1
2 3"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """5 5
1 2
2 3
3 4
3 5
1 5"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """13 16
7 9
7 11
3 8
1 13
11 11
6 11
8 13
2 11
3 3
8 12
9 11
1 11
5 13
3 12
6 9
1 10"""
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
