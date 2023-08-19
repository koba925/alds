import sys

sys.setrecursionlimit(2000000)

def sign_up_requests(N, S):
    ans = []
    names = set()
    for day, name in enumerate(S, start = 1):
        if name not in names:
            ans.append(day)
            names.add(name)
    return ans

def resolve():
    N = int(sys.stdin.readline())
    S = [sys.stdin.readline().strip() for _ in range(N)]
    print(*sign_up_requests(N, S), sep="\n")

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
        input = """5
e869120
atcoder
e869120
square1001
square1001"""
        output = """1
2
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
taro
hanako
yuka
takashi"""
        output = """1
2
3
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120
square869120"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
