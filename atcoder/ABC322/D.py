# TODO: get AC

# def trim(P):
#     Q = []
#     for r in P:
#         for c in r:
#             if c == "#":
#                 Q.append(r)
#                 break
#     R = []
#     for r in zip(*Q):
#         for c in r:
#             if c == "#":
#                 R.append(r)
#                 break
#     return list(zip(*R))


# def rot(P):
#     ph, pw = len(P), len(P[0])
#     Q = [["."] * ph for _ in range(pw)]
#     for r in range(ph):
#         for c in range(pw):
#             Q[c][ph - 1 - r] = P[r][c]
#     return Q


# def place(B, P, top, left):
#     for r in range(len(P)):
#         for c in range(len(P[0])):
#             if B[top + r][left + c] == P[r][c] == "#":
#                 return False
#             elif B[top + r][left + c] == ".":
#                 B[top + r][left + c] = P[r][c]
#     return True


# def polyomino(P1, P2, P3):
#     for _ in range(4):
#         for _ in range(4):
#             for top1 in range(0, 4 - len(P1) + 1):
#                 for left1 in range(0, 4 - len(P1[0]) + 1):
#                     B1 = [["."] * 4 for _ in range(4)]
#                     place(B1, P1, top1, left1)

#                     for top2 in range(0, 4 - len(P2) + 1):
#                         for left2 in range(0, 4 - len(P2[0]) + 1):
#                             B2 = [row[:] for row in B1]
#                             if not place(B2, P2, top2, left2):
#                                 continue

#                             for top3 in range(0, 4 - len(P3) + 1):
#                                 for left3 in range(0, 4 - len(P3[0]) + 1):
#                                     B3 = [row[:] for row in B2]
#                                     if not place(B3, P3, top3, left3):
#                                         continue
#                                     if all([all([c == "#" for c in r]) for r in B3]):
#                                         return True
#             P3 = rot(P3)
#         P2 = rot(P2)
#     return False


# def resolve():
#     P1 = [list(input()) for _ in range(4)]
#     P2 = [list(input()) for _ in range(4)]
#     P3 = [list(input()) for _ in range(4)]
#     P1 = trim(P1)
#     P2 = trim(P2)
#     P3 = trim(P3)

#     print("Yes" if polyomino(P1, P2, P3) else "No")


import itertools as it


def total(P):
    return sum([sum(r) for r in P])


def rot(P):
    Q = [[0] * 4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            Q[c][3 - r] = P[r][c]
    return Q


def place(B, P, top, left):
    NB = [r[:] for r in B]
    for r in range(4):
        for c in range(4):
            if P[r][c] == 0:
                continue
            if NB[top + r][left + c] == 1:
                return False
            NB[top + r][left + c] = 1
    return NB


def filled(B):
    for r in range(3, 7):
        for c in range(3, 7):
            if B[r][c] == 0:
                return False
    return True


def print_matrix(M):
    for r in range(len(M)):
        for c in range(len(M[1])):
            print(M[r][c], end="")
        print()


def polyomino(P1, P2, P3):
    if total(P1) + total(P2) + total(P3) != 16:
        return False

    B = [[0] * 10 for _ in range(10)]
    for _rot2 in range(4):
        for _rot3 in range(4):
            for t1, l1 in it.product(range(7), repeat=2):
                B1 = place(B, P1, t1, l1)
                for t2, l2 in it.product(range(7), repeat=2):
                    B2 = place(B1, P2, t2, l2)
                    if not B2:
                        continue
                    for t3, l3 in it.product(range(7), repeat=2):
                        B3 = place(B2, P3, t3, l3)
                        if not B3:
                            continue
                        if filled(B3):
                            return True
            P3 = rot(P3)
        P2 = rot(P2)
    return False


def resolve():
    P1 = [[0 if c == "." else 1 for c in input()] for _ in range(4)]
    P2 = [[0 if c == "." else 1 for c in input()] for _ in range(4)]
    P3 = [[0 if c == "." else 1 for c in input()] for _ in range(4)]

    print("Yes" if polyomino(P1, P2, P3) else "No")


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
        input = """\
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
####
"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_1(self):
        input = """....
###.
.#..
....
....
.###
.##.
....
..#.
.##.
.##.
.##."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """###.
#.#.
##..
....
....
..#.
....
....
####
##..
#...
#..."""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """##..
#..#
####
....
....
##..
.##.
....
.#..
.#..
.#..
.#.."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """....
..#.
....
....
....
..#.
....
....
....
..#.
....
...."""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """....
####
#...
#...
....
####
...#
..##
....
..##
..#.
..##"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """###.
.##.
..#.
.###
....
...#
..##
...#
....
#...
#...
#..."""
        output = """Yes"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
