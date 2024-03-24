import sys
from io import StringIO
import unittest

def resolve_firsttry():
    W, B = [int(e) for e in input().split()]
    keys = "wbwbwwbwbwbw"
    wbs = set()
    for i in range(len(keys)):
        for j in range(i, len(keys)):
            wbs.add((keys[i:j].count("w"), keys[i:j].count("b")))

    octaves = W // 7
    if (W - octaves * 7, B - octaves * 5) in wbs:
        print("Yes")
    else:
        print("No")

def resolve():
    W, B = [int(e) for e in input().split()]
    keys = "wbwbwwbwbwbw" * 20
    for i in range(len(keys) - W - B + 1):
        k = keys[i: i + W + B]
        if k.count("w") == W and k.count("b") == B:
            print("Yes")
            break
    else:
        print("No")

class TestClass(unittest.TestCase):
    def test_my_1(self):
        input = """1 0"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_my_2(self):
        input = """0 1"""
        output = """Yes"""
        self.assertIO(input, output)
    
    def test_sample1(self):
        input = """3 2"""
        expected = """Yes"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """3 0"""
        expected = """No"""
        self.assertIO(input, expected)

    def test_sample3(self):
        input = """92 66"""
        expected = """Yes"""
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
    unittest.main()
