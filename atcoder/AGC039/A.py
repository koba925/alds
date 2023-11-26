def resolve():
    def ops(S):
        ret, sub, prev = 0, 0, ""
        for s in S + "Z":
            if s != prev:
                ret += sub // 2
                sub = 0
            sub += 1
            prev = s
        return ret

    S, K = input(), int(input())

    if len(set(S)) == 1:
        print(len(S) * K // 2)
    else:
        ops1 = ops(S)
        ops2 = ops(S + S)
        print(ops1 + (ops2 - ops1) * (K - 1))

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
        input = """iissi
2"""
        output = """4"""
        self.assertIO(input, output)
    
    def test_2(self):
        input = """iiissi
2"""
        output = """5"""
        self.assertIO(input, output)
    
    def test_3(self):
        input = """iissiii
2"""
        output = """6"""
        self.assertIO(input, output)
    
    def test_4(self):
        input = """iiissiii
2"""
        output = """7"""
        self.assertIO(input, output)
    
    def test_5(self):
        input = """a
1"""
        output = """0"""
        self.assertIO(input, output)
    
    def test_6(self):
        input = """a
2"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_7(self):
        input = """a
3"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_8(self):
        input = """a
4"""
        output = """2"""
        self.assertIO(input, output)
    
    def test_9(self):
        input = """qq
1"""
        output = """1"""
        self.assertIO(input, output)
    
    def test_10(self):
        input = """qq
2"""
        output = """2"""
        self.assertIO(input, output)
    
    def test_14(self):
        input = """qq
3"""
        output = """3"""
        self.assertIO(input, output)
    
    def test_15(self):
        input = """qq
4"""
        output = """4"""
        self.assertIO(input, output)

    def test_11(self):
        input = """ab
1"""
        output = """0"""
        self.assertIO(input, output)

    def test_12(self):
        input = """ab
2"""
        output = """0"""
        self.assertIO(input, output)

    def test_16(self):
        input = """aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
999999999"""
        output = """49499999950"""
        self.assertIO(input, output)
    
    def test_13(self):
        input = """ab
3"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """issii
2"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """qq
81"""
        output = """81"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """cooooooooonteeeeeeeeeest
999993333"""
        output = """8999939997"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
