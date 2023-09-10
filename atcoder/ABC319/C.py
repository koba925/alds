import sys

import itertools as it


def resolve_mine():
    def is_gakkari(O):
        for r in range(3):
            if C[r][0] == C[r][1] and O[r][0] < O[r][2] and O[r][1] < O[r][2]:
                return True
            if C[r][1] == C[r][2] and O[r][1] < O[r][0] and O[r][2] < O[r][0]:
                return True
            if C[r][2] == C[r][0] and O[r][2] < O[r][1] and O[r][0] < O[r][1]:
                return True
        for c in range(3):
            if C[0][c] == C[1][c] and O[0][c] < O[2][c] and O[1][c] < O[2][c]:
                return True
            if C[1][c] == C[2][c] and O[1][c] < O[0][c] and O[2][c] < O[0][c]:
                return True
            if C[2][c] == C[0][c] and O[2][c] < O[1][c] and O[0][c] < O[1][c]:
                return True

        if C[0][0] == C[1][1] and O[0][0] < O[2][2] and O[1][1] < O[2][2]:
            return True
        if C[1][1] == C[2][2] and O[1][1] < O[0][0] and O[2][2] < O[0][0]:
            return True
        if C[2][2] == C[0][0] and O[2][2] < O[1][1] and O[0][0] < O[1][1]:
            return True

        if C[2][0] == C[1][1] and O[2][0] < O[0][2] and O[1][1] < O[0][2]:
            return True
        if C[1][1] == C[0][2] and O[1][1] < O[2][0] and O[0][2] < O[2][0]:
            return True
        if C[0][2] == C[2][0] and O[0][2] < O[1][1] and O[2][0] < O[1][1]:
            return True

        return False

    C = [[int(e) for e in sys.stdin.readline().split()] for _ in range(3)]

    total, gakkari = 0, 0
    for O in it.permutations(range(9)):
        total += 1
        if is_gakkari([O[0:3], O[3:6], O[6:9]]):
            gakkari += 1

    print(f"{1 - gakkari / total:.9f}")


def resolve():
    lines = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def is_gakkari(O):
        for line in lines:
            if (
                C[line[0]] == C[line[1]]
                and O[line[0]] < O[line[2]]
                and O[line[1]] < O[line[2]]
            ):
                return True
            if (
                C[line[1]] == C[line[2]]
                and O[line[1]] < O[line[0]]
                and O[line[2]] < O[line[0]]
            ):
                return True
            if (
                C[line[2]] == C[line[0]]
                and O[line[2]] < O[line[1]]
                and O[line[0]] < O[line[1]]
            ):
                return True
        return False

    C = [[int(e) for e in sys.stdin.readline().split()] for _ in range(3)]
    C = sum(C, [])

    total, gakkari = 0, 0
    for O in it.permutations(range(9)):
        total += 1
        if is_gakkari(O):
            gakkari += 1

    print(f"{1 - gakkari / total:.9f}")


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
        input = """3 1 9
2 5 6
2 7 1"""
        output = """0.666666666666666666666666666667"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7 7 6
8 6 8
7 7 6"""
        output = """0.004982363315696649029982363316"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 6 7
1 9 7
5 7 5"""
        output = """0.4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
