import sys
import collections as cl


def resolve_counter():
    N = int(sys.stdin.readline())
    C = cl.Counter([sys.stdin.readline().strip() for _ in range(N)])
    K = C.most_common(1)[0][1]
    print(*sorted([name for name, count in C.items() if count == K]), sep="\n")


def resolve():
    N = int(sys.stdin.readline())
    d = cl.defaultdict(int)
    for _ in range(N):
        S = sys.stdin.readline().strip()
        d[S] += 1
    maxpoll = max(d.values())
    print(*sorted(name for name, poll in d.items() if poll == maxpoll), sep="\n")


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
        input = """7
beat
vet
beet
bed
vet
bet
beet"""
        output = """beet
vet"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo
buffalo"""
        output = """buffalo"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
bass
bass
kick
kick
bass
kick
kick"""
        output = """kick"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """4
ushi
tapu
nichia
kun"""
        output = """kun
nichia
tapu
ushi"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
