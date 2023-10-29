def resolve():
    import itertools as it

    def dfs(k):    
        def comform_row():
            for ci in range(N):                       
                if row[ci] != ".":
                    return row[ci] == R[k]
                    
        def comform_columns():
            for ci in range(N):
                for ri in range(k):                       
                    if B[ri][ci] != ".":
                        if B[ri][ci] != C[ci]:
                            return False
                        break
            return True

        def comform_once():
            for ci in range(N):
                a = b = c = 0
                for ri in range(N):                       
                    match B[ri][ci]:
                        case "A": a += 1
                        case "B": b += 1
                        case "C": c += 1
                if not (a == b == c == 1):
                    return False
            return True

        if not comform_columns(): return False
        if k == N: return comform_once()
        
        for row in it.permutations("ABC" + "." * (N - 3)):
            if not comform_row(): continue
            B.append(row)
            result = dfs(k + 1)
            if result:
                return True
            B.pop()
        return False

    N = int(input())
    R = input()
    C = input()

    B = []
    result = dfs(0)
    if result:
        print("Yes")
        for r in B:
            print("".join(r))
    else:
        print("No")

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

    def test_1(self):
        input = """3
ABC
ACB"""
        output = """Yes
ACB
BAC
CBA"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
ABCBC
ACAAB"""
        output = """Yes
AC..B
.BA.C
C.BA.
BA.C.
..CBA"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """3
AAA
BBB"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
