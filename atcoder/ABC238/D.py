import sys

sys.setrecursionlimit(2000000)

def to_bin(n):
    b = []
    while n > 0:
        b.append(n % 2)
        n //= 2
    return b

def and_and_sum_mine(a, s):
    ba, bs = to_bin(a), to_bin(s)
    la, ls = len(ba), len(bs)
    if la != 0 and ls < la + 1:
        return False
    ba += [0] * (ls - la)
    carry = 0
    for i in range(ls):
        if ba[i] == 1:
            if (carry == 0 and bs[i] == 1) or (carry == 1 and bs[i] == 0) :
                return False
            carry = 1
        else:
            carry = 1 if carry == 1 and bs[i] == 0 else 0
    return True

def and_and_sum_editorial(a, s):
    # x = a + x'、y = a + y'、t = x' + y' とおく
    # s = x + y = 2a + x' + y' = 2a + t より
    t = s - 2 * a
    # t = x' + y' >= 0 であることが必要
    # さらに    
    # x AND y = a で
    # x や y から a を引いたのが x' や y' ということは、
    # x + y を計算したときに繰り上がる箇所をなくしたのが
    # x' や y' ということ
    # あとは桁ごとに見ていけばよい
    # t の桁が 0 なら x' と y' を両方 0 にすればよい
    # t の桁が 1 で
    # a の桁が 0 なら x' と y' を 1,0 か 0,1 にすればよい
    # a の桁が 1 のときは x' と y' を両方 1 にする必要があるが定義と矛盾
    # t と a が両方1になるような桁があると x'、y' を作れない
    return t >= 0 and t & a == 0

def resolve():
    T = int(sys.stdin.readline())
    for _ in range(T):
        a, s = [int(e) for e in sys.stdin.readline().split()]
        # print("Yes" if and_and_sum_mine(a, s) else "No")
        print("Yes" if and_and_sum_editorial(a, s) else "No")

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
        input = """2
1 8
4 2"""
        output = """Yes
No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
201408139683277485 381410962404666524
360288799186493714 788806911317182736
18999951915747344 451273909320288229
962424162689761932 1097438793187620758"""
        output = """No
Yes
Yes
No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
