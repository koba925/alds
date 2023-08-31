import sys

import collections as cl


def resolve_deque():
    def print_front(i):
        if len(q) < i:
            print("ERROR")
        else:
            print(q[i - 1])
            del q[i - 1]

    def print_back(i):
        if len(q) < i:
            print("ERROR")
        else:
            print(q[-i])
            del q[-i]

    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()

    q = cl.deque()
    for i, s in enumerate(S, 1):
        if s == "L":
            q.appendleft(i)
        elif s == "R":
            q.append(i)
        elif s == "A":
            print_front(1)
        elif s == "B":
            print_front(2)
        elif s == "C":
            print_front(3)
        elif s == "D":
            print_back(1)
        elif s == "E":
            print_back(2)
        elif s == "F":
            print_back(3)


# 解説をコピー dequeの方が高速
# マイナスの添え字の扱いがうまくハマってこれでうまくいくわけか
def resolve_editorial():
    N = int(input())
    S = input()
    a = [0] * N
    l = 0
    r = 0
    for i in range(N):
        c = S[i]
        if c == "L":
            l -= 1
            a[l] = i + 1
        elif c == "R":
            a[r] = i + 1
            r += 1
        elif ord(c) < 68:
            x = ord(c) - 65
            if r - l <= x:
                print("ERROR")
                continue
            print(a[l + x])
            for j in range(x, 0, -1):
                a[l + j] = a[l + j - 1]
            l += 1
        else:
            x = ord(c) - 68
            if r - l <= x:
                print("ERROR")
                continue
            print(a[r - 1 - x])
            for j in range(x, 0, -1):
                a[r - 1 - j] = a[r - j]
            r -= 1


# 確かめつつ自分で書いてみる
def resolve():
    def qlen():
        return r - l

    def print_front(k):
        nonlocal l

        if qlen() < k:
            print("ERROR")
        else:
            print(q[l + k - 1])
            while k > 1:
                q[l + k - 1] = q[l + k - 2]
                k -= 1
            l += 1

    def print_back(k):
        nonlocal r

        if qlen() < k:
            print("ERROR")
        else:
            print(q[r - k])
            while k > 1:
                q[r - k] = q[r - k + 1]
                k -= 1
            r -= 1

    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()

    q, l, r = [0] * N, 0, 0

    for i, s in enumerate(S, 1):
        if s == "L":
            l -= 1
            q[l] = i
        elif s == "R":
            q[r] = i
            r += 1
        elif s == "A":
            print_front(1)
        elif s == "B":
            print_front(2)
        elif s == "C":
            print_front(3)
        elif s == "D":
            print_back(1)
        elif s == "E":
            print_back(2)
        elif s == "F":
            print_back(3)


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
        input = """11
LLRLRCDEFBA"""
        output = """1
5
2
ERROR
3
4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """36
RLLDBBDDLCLDFRLRRLRRFLRDRLALLELCAARF"""
        output = """1
2
ERROR
3
ERROR
ERROR
9
ERROR
17
23
26
20
28
31
29
19"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
