def resolve_greedy():
    N, K = [int(e) for e in input().split()]
    R, S, P = [int(e) for e in input().split()]
    T = input()

    point, hands = 0, ["-"] * N
    for i, t in enumerate(T):
        if t == "r" and not (K <= i and hands[i - K] == "p"):
            point += P
            hands[i] = "p"
        elif t == "s" and not (K <= i and hands[i - K] == "r"):
            point += R
            hands[i] = "r"
        elif t == "p" and not (K <= i and hands[i - K] == "s"):
            point += S
            hands[i] = "s"
    print(point)

# resolve()
# exit()

def resolve():
    def point(cpu):
        l = len(cpu)
        memo = [{"r": 0, "s": 0, "p": 0} for _ in range(l + 1)]

        for i, t in enumerate(cpu, 1):
            memo[i]["r"] = max(memo[i - 1]["s"], memo[i - 1]["p"])
            memo[i]["s"] = max(memo[i - 1]["p"], memo[i - 1]["r"]) 
            memo[i]["p"] = max(memo[i - 1]["r"], memo[i - 1]["s"])
            match t:
                case "r": memo[i]["p"] += P
                case "s": memo[i]["r"] += R
                case "p": memo[i]["s"] += S
        return max(memo[l].values())

    N, K = [int(e) for e in input().split()]
    R, S, P = [int(e) for e in input().split()]
    T = input()

    print(sum(point(T[m::K]) for m in range(K)))

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
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr"""
        output = """4996"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
