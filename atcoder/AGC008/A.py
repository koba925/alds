def resolve_mine():
    x, y = [int(e) for e in input().split()]

    if x == 0 and 0 < y:
        print(abs(y - x))
    elif x == 0 and y < 0:
        print(abs(y - x) + 1)
    elif y == 0 and 0 < x:
        print(abs(y - x) + 1)
    elif y == 0 and x < 0:
        print(abs(y - x))
    elif 0 <= x <= y or x <= y <= 0:
        print(abs(y - x))
    elif 0 <= y <= x or y <= x <= 0:
        print(1 + abs(y - x) + 1)
    else:
        print(abs(y + x) + 1)

def resolve():
    x, y = [int(e) for e in input().split()]

    ans = float("inf")
    if x <= y: 
        ans = min(ans, y - x)
    if -x <= y:
        ans = min(ans, 1 + y + x)
    if x <= -y:
        ans = min(ans, -y - x + 1)
    if y <= x:
        ans = min(ans, x - y + 2)
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

    def test_1(self):
        input = """-5 -3"""
        output = """2"""
        self.assertIO(input, output)
    
    def test_2(self):
        input = """-3 -5"""
        output = """4"""
        self.assertIO(input, output)

    def test_3(self):
        input = """-3 -3"""
        output = """0"""
        self.assertIO(input, output)
        
    def test_4(self):
        input = """-3 5"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_5(self):
        input = """-5 3"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_6(self):
        input = """-3 3"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_7(self):
        input = """3 -5"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_8(self):
        input = """5 -3"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_9(self):
        input = """3 -3"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_10(self):
        input = """3 5"""
        output = """2"""
        self.assertIO(input, output)
    
    def test_11(self):
        input = """5 3"""
        output = """4"""
        self.assertIO(input, output)
    
    def test_12(self):
        input = """3 3"""
        output = """0"""
        self.assertIO(input, output)
    
    def test_13(self):
        input = """-1 0"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_14(self):
        input = """1 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_15(self):
        input = """0 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_16(self):
        input = """0 -1"""
        output = """2"""
        self.assertIO(input, output)
        
    def test_入力例_1(self):
        input = """10 20"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 -10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-10 -20"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
