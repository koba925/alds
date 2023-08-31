import sys
import collections as cl


def resolve_mine():
    S = sys.stdin.readline().strip()
    T = cl.deque()
    is_reversed = False

    for s in S:
        if s == "R":
            is_reversed = not is_reversed
        else:
            (T.appendleft if is_reversed else T.append)(s)

    if is_reversed:
        T = reversed(T)

    i, U = 0, cl.deque()
    for t in T:
        U.append(t)
        if len(U) >= 2 and U[-2] == U[-1]:
            U.pop()
            U.pop()

    print("".join(U))


def resolve():
    T, rev = cl.deque(), False
    for i, s in enumerate(sys.stdin.readline().strip()):
        if s == "R":
            rev = not rev
        elif rev:
            if T and s == T[0]:
                T.popleft()
            else:
                T.appendleft(s)
        else:
            if T and s == T[-1]:
                T.pop()
            else:
                T.append(s)

    if rev:
        T.reverse()

    print("".join(T))


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
        input = """ozRnonnoe"""
        output = """zone"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hellospaceRhellospace"""
        output = """"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
