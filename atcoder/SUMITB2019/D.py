def resolve():
    import itertools as it

    N = int(input())
    S = input()

    pin = set()
    for a, b, c in it.combinations(S, 3):
        pin.add((a, b, c))
    print(len(pin))

def resolve():
    N = int(input())
    S = input()

    pins = 0
    for l in range(1000):
        d = f"{l:03d}"
        i = 0
        for s in (S):
            if d[i] == s:
                i += 1
                if i == 3:
                    pins += 1
                    break
    print(pins)

def resolve_():
    N = int(input())
    S = input()

    ans = 0
    for a in "0123456789":
        i = 0
        while i < N and S[i] != a: i += 1
        if i == N: continue
        for b in "0123456789":
            j = i + 1
            while j < N and S[j] != b: j += 1
            if j == N: continue
            for c in "0123456789":
                k = j + 1
                while k < N and S[k] != c: k += 1
                if k == N: continue
                ans += 1

    print(ans)

# resolve()
# exit()



# resolve()
# exit()


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
        input = """4
0224"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
123123"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19
3141592653589793238"""
        output = """329"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
