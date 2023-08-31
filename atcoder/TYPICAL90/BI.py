import sys

import collections as cl


def resolve():
    Q = int(sys.stdin.readline())
    q = cl.deque()
    for _ in range(Q):
        t, x = [int(e) for e in sys.stdin.readline().split()]
        if t == 1:
            q.appendleft(x)
        elif t == 2:
            q.append(x)
        else:
            print(q[x - 1])


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
1 2
1 1
2 3
3 1
3 2
3 3"""
        output = """1
2
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
2 1
3 1
2 2
3 1
2 3
3 1"""
        output = """1
1
1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
1 1000000000
2 200000000
1 30000000
2 4000000
1 500000
3 3"""
        output = """1000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

# import sys

# from collections import deque

# def resolve_deque():
#     Q = int(sys.stdin.readline())
#     cards = deque()
#     for _ in range(Q):
#         t, x = [int(e) for e in sys.stdin.readline().split()]
#         if t == 1:
#             cards.appendleft(x)
#         elif t == 2:
#             cards.append(x)
#         elif t == 3:
#             print(cards[x - 1])

# def resolve_list_TLE():
#     Q = int(sys.stdin.readline())
#     cards = []
#     for _ in range(Q):
#         t, x = [int(e) for e in sys.stdin.readline().split()]
#         if t == 1:
#             cards = [x] + cards
#         elif t == 2:
#             cards = cards + [x]
#         elif t == 3:
#             print(cards[x - 1])

# class DequeList:
#     def __init__(self, size):
#         self.size = size
#         self.list = [None] * (size * 2)
#         self.left = size
#         self.right = size

#     def __getitem__(self, i):
#         return self.list[self.left + i]

#     def __repr__(self):
#         return f"DequeList({self.left}, {self.right}, {self.list})"

#     def __str__(self):
#         return str(self.list[self.left:self.right])

#     def append(self, val):
#         self.list[self.right] = val
#         self.right += 1

#     def pop(self):
#         self.right -= 1
#         return self.list[self.right]

#     def appendleft(self, val):
#         self.left -= 1
#         self.list[self.left] = val

#     def popleft(self):
#         self.left += 1
#         return self.list[self.left - 1]

# def resolve():
#     Q = int(sys.stdin.readline())
#     cards = DequeList(Q)
#     for _ in range(Q):
#         t, x = [int(e) for e in sys.stdin.readline().split()]
#         if t == 1:
#             cards.appendleft(x)
#         elif t == 2:
#             cards.append(x)
#         elif t == 3:
#             print(cards[x - 1])

# resolve()
# exit()
