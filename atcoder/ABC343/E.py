def resolve():
    def solve(V):
        all = 7 ** 3 * 3
        a1 = b1 = c1 = 0
        for a2 in range(21):
            a12 = max(0, a1 + 7 - a2)
            for b2 in range(21):
                b12 = max(0, b1 + 7 - b2)
                for c2 in range(21):
                    c12 = max(0, c1 + 7 - c2)
                    int12 = a12 * b12 * c12
                    for a3 in range(21):
                        a13 = max(0, a1 + 7 - a3)
                        for b3 in range(21):
                            b13 = max(0, b1 + 7 - b3)
                            for c3 in range(21):
                                c13 = max(0, c1 + 7 - c3)
                                int13 = a13 * b13 * c13

                                a23 = max(0, min(a2, a3) + 7 - max(a2, a3))
                                b23 = max(0, min(b2, b3) + 7 - max(b2, b3))
                                c23 = max(0, min(c2, c3) + 7 - max(c2, c3))
                                int23 = a23 * b23 * c23
                                
                                a123 = max(0, min(a1, a2, a3) + 7 - max(a1, a2, a3))
                                b123 = max(0, min(b1, b2, b3) + 7 - max(b1, b2, b3))
                                c123 = max(0, min(c1, c2, c3) + 7 - max(c1, c2, c3))
                                int123 = a123 * b123 * c123

                                if int123 != V[2]: continue
                                int2 = int12 + int13 + int23
                                V1 = int2 - 2 * int123
                                if V1 != V[1]: continue
                                if all - int2 + int123 != V[0]:continue
                                return [0, 0, 0, a2, b2, c2, a3, b3, c3]
        return []
    
    ans = solve([int(e) for e in input().split()])
    if ans == []:
        print("No")
    else:
        print("Yes")
        print(*ans)

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
        input = """840 84 7"""
        output = """Yes
0 0 0 0 6 0 6 0 0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """343 34 3"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
