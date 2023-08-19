import sys

from collections import defaultdict

def peaceful_teams_editorial1(N, T, M, dislikes):
    def dfs(p):
        if p > N:
            return 1 if len(teams) == T else 0

        ans = 0        

        for team in teams:
            if dislikes[p].isdisjoint(team):
                team.add(p)
                ans += dfs(p + 1)
                team.remove(p)

        if len(teams) < T:
            teams.append({p})
            ans += dfs(p + 1)
            teams.pop()

        return ans
    
    teams = []
    return dfs(1)

def resolve_editorial1():
    N, T, M = [int(e) for e in sys.stdin.readline().split()]
    dislikes = defaultdict(set)
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()] 
        dislikes[a].add(b)
        dislikes[b].add(a)
    print(peaceful_teams_editorial1(N, T, M, dislikes))

class BitSet:

    def __init__(self, size: int, bits: int=0) -> None:
        self.size: int = size
        self.mask: int = 2 ** size - 1
        self.bits: int = bits

    def __str__(self) -> str:
        return f"{self.bits:0{self.size}b}"

    def __repr__(self) -> str:
        return f"BitSet({self.bits:0{self.size}b})"

    def __len__(self) -> int:
        bs, c = self.bits, 0
        for _ in range(self.size):
            c += bs & 1
            bs >>= 1
        return c
    
    def __eq__(self, other: "BitSet") -> bool:
        assert self.size == other.size
        return self.bits == other.bits
    
    def __ne__(self, other: "BitSet") -> bool:
        assert self.size == other.size
        return self.bits != other.bits

    def __contains__(self, i: int) -> bool:
        return self.bits >> i & 1 != 0

    def __and__(self, other: "BitSet") -> "BitSet":
        return self.intersection(other)

    def __or__(self, other: "BitSet") -> "BitSet":
        return self.union(other)
    
    def __sub__(self, other: "BitSet") -> "BitSet":
        return self.union(other)
    
    def __le__(self, other: "BitSet") -> bool:
        return self.issubset(other)

    def __lt__(self, other: "BitSet") -> bool:
        assert self.size == other.size
        return self <= other and self != other
    
    def __ge__(self, other: "BitSet") -> bool:
        return self.issuperset(other)

    def __gt__(self, other: "BitSet") -> bool:
        assert self.size == other.size
        return self >= other and self != other
         
    def add(self, i: int) -> "BitSet":
        self.bits |= 1 << i
        return self
    
    def discard(self, i: int) -> "BitSet":
        self.bits &= (1 << i ^ self.mask)
        return self

    def clear(self) -> "BitSet":
        self.bits = 0
        return self

    def intersection(self, other: "BitSet") -> "BitSet":
        assert self.size == other.size
        return BitSet(self.size, self.bits & other.bits)

    def union(self, other: "BitSet") -> "BitSet":
        assert self.size == other.size
        return BitSet(self.size, self.bits | other.bits)

    def flip(self, i: int) -> "BitSet":
        self.bits ^= self.mask
        return self
    
    def difference(self, other: "BitSet") -> "BitSet":
        assert self.size == other.size
        return BitSet(self.size, self.bits & other.flip().bits)

    def symmetric_difference(self, other: "BitSet") -> "BitSet":
        assert self.size == other.size
        return BitSet(self.size, self.bits ^ other.bits)
    
    def issubset(self, other: "BitSet") -> bool:
        assert self.size == other.size
        return self.bits & other.bits == self.bits
    
    def issuperset(self, other: "BitSet") -> bool:
        assert self.size == other.size
        return self.bits & other.bits == other.bits

    def isempty(self):
        return self.bits == 0
    
    def isdisjoint(self, other: "BitSet") -> bool:
        return (self & other).isempty()

def peaceful_teams_bitset(N, T, M, dislikes):
    def dfs(p):
        if p == N:
            return 1 if len(teams) == T else 0

        ans = 0        

        for team in teams:
            if dislikes[p].isdisjoint(team):
                team.add(p)
                ans += dfs(p + 1)
                team.discard(p)

        if len(teams) < T:
            team = BitSet(N)
            team.add(p)
            teams.append(team)
            ans += dfs(p + 1)
            teams.pop()

        return ans
    
    teams = []
    return dfs(0)

def resolve():
    N, T, M = [int(e) for e in sys.stdin.readline().split()]
    dislikes = [BitSet(N) for _ in range(N)]
    for _ in range(M):
        a, b = [int(e) for e in sys.stdin.readline().split()] 
        dislikes[a - 1].add(b - 1)
        dislikes[b - 1].add(a - 1)
    print(peaceful_teams_bitset(N, T, M, dislikes))

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
        input = """5 2 2
1 3
3 4"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 1 2
1 3
3 4"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 4 0"""
        output = """65"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 6 8
5 9
1 4
3 8
1 6
4 10
5 7
5 6
3 7"""
        output = """8001"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
