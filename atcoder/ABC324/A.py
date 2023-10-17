def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]
    print("Yes" if all(a == A[0] for a in A) else "No")

def resolve():
    N = int(input())
    A = [int(e) for e in input().split()]

    for a in A:
        for b in A:
            if a != b:
                print("No")
                break
        else:
            continue
        break
    else:
        print("Yes")
        
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
3 2 4"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
3 3 3 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
73 8 55 26 97 48 37 47 35 55"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
