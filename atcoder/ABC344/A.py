# TK: 正規表現 Regular Expression https://docs.python.org/ja/3.10/library/re.html

import sys
from io import StringIO
import unittest

import re

def resolve_contest():
    inside = False

    for s in input():
        if s == "|":
            inside = not inside
            continue
        if not inside:
            print(s, end="")
    print()


def resolve():
    print(re.sub(r"\|.*\|", "", input()))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """atcoder|beginner|contest"""
        expected = """atcodercontest"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """|spoiler|"""
        expected = """"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """||xyz"""
        expected = """xyz"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    resolve()
