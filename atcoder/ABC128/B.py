import sys
import collections as cl
import operator as op


def resolve_1():
    restaurants = cl.defaultdict(list)
    N = int(sys.stdin.readline())

    for i in range(1, N + 1):
        s, p = sys.stdin.readline().split()
        restaurants[s].append((int(p), i))

    for s in sorted(restaurants.keys()):
        for _, i in reversed(sorted(restaurants[s])):
            print(i)


def resolve_2():
    N = int(sys.stdin.readline())
    restaurants = []
    for i in range(1, N + 1):
        s, p = sys.stdin.readline().split()
        restaurants.append((s, -int(p), i))

    restaurants.sort()
    for _, _, i in restaurants:
        print(i)


def resolve():
    N = int(sys.stdin.readline())
    restaurants = []
    for i in range(1, N + 1):
        s, p = sys.stdin.readline().split()
        restaurants.append((s, int(p), i))

    restaurants.sort(key=op.itemgetter(1), reverse=True)
    restaurants.sort(key=op.itemgetter(0))

    for _, _, i in restaurants:
        print(i)


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
        input = """6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40"""
        output = """3
4
6
1
5
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
yakutsk 10
yakutsk 20
yakutsk 30
yakutsk 40
yakutsk 50
yakutsk 60
yakutsk 70
yakutsk 80
yakutsk 90
yakutsk 100"""
        output = """10
9
8
7
6
5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
