def resolve():
    N, K = [int(e) for e in input().split()]
    A = [int(e) for e in input().split()]
    B = set(A)
    ans = K
    for i in range(K):
        if i not in B:
            ans = i
            break
    print(ans)

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

    def test_my_1(self):
        input = """3 5
0 1 2"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_入力例_1(self):
        input = """7 3
2 0 2 3 2 1 9"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
