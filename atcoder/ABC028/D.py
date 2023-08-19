import sys

def random_generation(N, K):
    # すべて
    all = N ** 3
    # すべてK
    all_k = 1
    # ふたつがK
    two_k = 3 * (N - 1)
    # すべて異なってまんなかがK
    center_k = ((K - 1) * (N - K)) * 6

    return (all_k + two_k + center_k) / all

def resolve():
    N, K = [int(e) for e in sys.stdin.readline().split()]    
    print(f"{random_generation(N, K):0.9f}")

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

    def test_入力例1(self):
        input = """3 2"""
        output = """0.48148148148148148148"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """3 1"""
        output = """0.25925925925925925926"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """765 573"""
        output = """0.00147697396984624371"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
