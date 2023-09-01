# LL: in演算子忘れがち

import sys


# def int_to_base_b(n: int, b: int) -> str:
#     if n == 0:
#         return "0"
#     d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     temp = []
#     while n > 0:
#         temp.append(d[n % b])
#         n //= b
#     return "".join(reversed(temp))
#
# def no_seven(s):
#     return s.find("7") == -1
#
# def resolve():
#     N = int(sys.stdin.readline())
#     count = 0
#     for n in range(1, N + 1):
#         if no_seven(str(n)) and no_seven(int_to_base_b(n, 8)):
#             count += 1
#     print(count)


def resolve():
    N = int(sys.stdin.readline())
    print(
        len([n for n in range(1, N + 1) if "7" not in str(n) and "7" not in oct(n)[2:]])
    )


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
        input = """20"""
        output = """17"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """100000"""
        output = """30555"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
