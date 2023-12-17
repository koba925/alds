def resolve():

    N = int(input())
    TX = [[int(e) for e in input().split()] for _ in range(N)]

    K = 0
    max_K = 0
    acts = []
    enemies = [0] * N

    for t, x in reversed(TX):
        x -= 1
        if t == 1:
            if enemies[x] > 0: 
                enemies[x] -= 1
                K -= 1
                acts.append(1)
            else:
                acts.append(0)       
        else: # t == 2
            enemies[x] += 1
            K += 1
            max_K = max(max_K, K)

    if sum(enemies) > 0:
        print(-1)
    else:
        print(max_K)
        print(*reversed(acts))

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
        input = """13
1 2
1 3
1 1
1 3
1 2
2 3
1 3
1 3
2 3
1 3
2 2
2 3
2 1"""
        output = """3
1 1 1 0 0 1 0 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
2 3
1 4
2 1
1 2"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30
1 25
1 2
1 10
1 18
2 18
1 11
2 11
1 21
1 6
2 2
2 10
1 11
1 24
1 11
1 3
1 2
1 18
2 25
1 8
1 10
1 11
2 18
2 10
1 10
2 2
1 24
1 10
2 10
1 25
2 6"""
        output = """4
1 1 1 1 1 1 0 1 1 0 0 0 0 1 0 0 1 0 0 0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
