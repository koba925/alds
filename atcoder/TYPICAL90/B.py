import sys

def is_balanced_stack(s):
    stack = []
    for p in s:
        if p == "(":
            stack.append(p)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0

def is_balanced(s):
    balance = 0
    for p in s:
        if p == "(":
            balance += 1
        else:
            balance -=1
            if balance < 0:
                return False
    return balance == 0

def encyclopedia_of_rec(N):
    def rec(s):
        if len(s) == N:
            if is_balanced(s):
                print(s)                
            return
        rec(s + "(")
        rec(s + ")")

    ans = 0
    rec("")

class Bits:

    def __init__(self, len: int, bits: int=0) -> None:
        self.length = len
        self.mask = 2 ** len - 1
        self.bits: int = bits

    def __str__(self) -> str:
        return f"{self.bits:0{self.length}b}"

    def __repr__(self) -> str:
        return f"Bits({self.bits:0{self.length}b})"

    def __getitem__(self, i: int) -> int:
        return self.test(i)

    def __setitem__(self, i: int, b: int) -> None:
        if b == 0:
            self.clear(i)
        else:
            self.set(i)

    def test(self, i: int) -> int:
        return self.bits >> i & 1

    def set(self, i: int) -> None:
        self.bits |= 1 << i

    def clear(self, i: int) -> None:
        self.bits &= (1 << i ^ self.mask)

    def flip(self, i: int) -> None:
        self.bits ^= 1 << i

    def all(self) -> int:
        return 1 if self.bits == self.mask else 0

    def any(self) -> int:
        return 1 if self.bits != 0 else 0

    def none(self) -> int:
        return 1 if self.bits == 0 else 0

    def count(self) -> int:
        bs, c = self.bits, 0
        for _ in range(self.length):
            c += bs & 1
            bs >>= 1
        return c

    def val(self) -> int:
        return self.bits
    
def encyclopedia_of_parentheses_bits(N):
    for n in range(2 ** N):
        bits = Bits(N, n)
        s = ""
        for i in reversed(range(N)):
            if bits[i] == 0:
                s += "("
            else:
                s += ")"
        if is_balanced(s):
            print(s)
        
def encyclopedia_of_parentheses(N):
    for n in range(2 ** N):
        s = ""
        balance = 0
        for i in reversed(range(N)):
            if n >> i & 1 == 0:
                s += "("
                balance += 1
            else:
                s += ")"
                balance -= 1
                if balance < 0:
                    break
        if balance == 0:
            print(s)

def resolve():
    N = int(sys.stdin.readline())    
    encyclopedia_of_parentheses_bits(N)

resolve()
exit()

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
        input = """2"""
        output = """()"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4"""
        output = """(())
()()"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10"""
        output = """((((()))))
(((()())))
(((())()))
(((()))())
(((())))()
((()(())))
((()()()))
((()())())
((()()))()
((())(()))
((())()())
((())())()
((()))(())
((()))()()
(()((())))
(()(()()))
(()(())())
(()(()))()
(()()(()))
(()()()())
(()()())()
(()())(())
(()())()()
(())((()))
(())(()())
(())(())()
(())()(())
(())()()()
()(((())))
()((()()))
()((())())
()((()))()
()(()(()))
()(()()())
()(()())()
()(())(())
()(())()()
()()((()))
()()(()())
()()(())()
()()()(())
()()()()()"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
