def resolve():
    N, M = [int(e) for e in input().split()]
    
    import collections as cl

    prefs = cl.defaultdict(lambda: [])
    for city in range(M):
        p, y = [int(e) for e in input().split()]
        prefs[p].append((y, city))
    
    for p in prefs:
        prefs[p].sort()

    numbers = [""] * M
    for p in prefs:
        for ber, [year, city] in enumerate(prefs[p], 1):
         numbers[city] = f"{p:06d}{ber:06d}"

    print(*numbers, sep="\n")

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
        input = """2 3
1 32
2 63
1 12"""
        output = """000001000002
000002000001
000001000001"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 3
2 55
2 77
2 99"""
        output = """000002000001
000002000002
000002000003"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
