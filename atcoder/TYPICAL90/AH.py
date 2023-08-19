import sys  # https://docs.python.org/ja/3/library/sys.html
from typing import Any

import collections as cl  # https://docs.python.org/ja/3/library/collections.html


class AutoDeleteDefaultDict(cl.defaultdict):
    def __setitem__(self, __key: Any, __value: Any) -> None:
        super().__setitem__(__key, __value)
        if not __value and __key in self:
            del self[__key]


def elements(N, K, A):
    numbers = AutoDeleteDefaultDict(int)
    left, right, maxlen = 0, 0, 0

    while True:
        while True:
            numbers[A[right]] += 1
            right += 1
            if len(numbers) > K:
                break
            maxlen = max(maxlen, right - left)
            if right == N:
                break
        numbers[A[left]] -= 1
        left += 1
        if right == N:
            break

    return maxlen


def elements(N, K, A):
    numbers = AutoDeleteDefaultDict(int)
    left, right, maxlen = 0, 0, 0

    while left < N:
        while right < N:
            if A[right] not in numbers and len(numbers) == K:
                break
            numbers[A[right]] += 1
            right += 1
        maxlen = max(maxlen, right - left)
        numbers[A[left]] -= 1
        left += 1

    return maxlen


def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]
    A = [int(e) for e in sys.stdin.readline().split()]
    print(elements(N, K, A))


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
        input = """5 1
1 2 3 4 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 4
1 1 2 4 2"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 2
1 2 3 4 4 3 2 1 2 3"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
