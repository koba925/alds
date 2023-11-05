def resolve():
    import sys
    sys.setrecursionlimit(1000000)

    def dfs(node):
        x = X[node]
        for nxt in G[node]:
            if X[nxt] == 2:
                X[nxt] = 1 - x
                result = dfs(nxt)
                if not result: return False
            elif X[nxt] != 1 - x: return False
        return True

    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    G = [[] for _ in range(N)]
    for a, b in zip(A, B):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    X = [2] * N
    for node in range(N):
        if X[node] != 2 or not G[node]: continue
        X[node] = 0
        if not dfs(node):
            print("No")
            break
    else:
        print("Yes")

# resolve()
# exit()

def resolve():
    def dfs(n):
        q = []
        q.append(n)
        X[n] = 0
        while q:
            n = q.pop()
            for m in G[n]:
                if X[m] == 2:
                    q.append(m)
                    X[m] = 1 - X[n]
                elif X[m] != 1 - X[n]:
                    return False
        return True

    N, M = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    G = [[] for _ in range(N)]
    for a, b in zip(A, B):
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)
    
    X = [2] * N
    for i in range(N):
        if X[i] != 2 or not G[i]: continue
        if not dfs(i):
            print("No")
            break
    else:
        print("Yes")                    

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
        input = """5 2
1 4
2 5"""
        output = """Yes"""
        self.assertIO(input, output)


    def test_2(self):
        input = """7 7
1 6 2 7 5 2 2
3 2 7 2 1 3 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3 2
1 2
2 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1 2 3
2 3 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 1
1
1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """7 8
1 6 2 7 5 4 2 2
3 2 7 2 1 2 3 3"""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
