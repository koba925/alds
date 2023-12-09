def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    B = [int(e) for e in input().split()]

    excesses = sorted([a - b for a, b in zip(A, B) if a > b], reverse=True)
    deficiencies = [b - a for a, b in zip(A, B) if a < b]

    ans = len(deficiencies)
    if ans > 0:
        def_total = sum(deficiencies)
        for excess in excesses:
            ans += 1
            def_total -= excess
            if def_total <= 0:
                break
        else:
            ans = -1

    print(ans)




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
        input = """3
2 3 5
3 4 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
2 3 3
2 2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3
17 7 1
25 6 14"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """12
757232153 372327760 440075441 195848680 354974235 458054863 463477172 740174259 615762794 632963102 529866931 64991604
74164189 98239366 465611891 362739947 147060907 118867039 63189252 78303147 501410831 110823640 122948912 572905212"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
