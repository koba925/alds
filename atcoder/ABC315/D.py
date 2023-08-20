# LL: 数で管理してオーダを減らす

import sys  # https://docs.python.org/ja/3/library/sys.html


def magical_cookies_mine(H, W, C):
    deleted = True
    while deleted:
        to_delete = [[False] * W for _ in range(H)]
        deleted = False

        for row in range(H):
            color = ""
            same_color = True
            count = 0
            for col in range(W):
                if C[row][col] == ".":
                    continue
                if color == "":
                    color = C[row][col]
                    count = 0
                elif color != C[row][col]:
                    break
                count += 1
            else:
                if count >= 2:
                    for col in range(W):
                        to_delete[row][col] = True
                    deleted = True

        for col in range(W):
            color = ""
            same_color = True
            count = 0
            for row in range(H):
                if C[row][col] == ".":
                    continue
                if color == "":
                    color = C[row][col]
                    count = 0
                elif color != C[row][col]:
                    break
                count += 1
            else:
                if count >= 2:
                    for row in range(H):
                        to_delete[row][col] = True
                    deleted = True

        for row in range(H):
            for col in range(W):
                if to_delete[row][col]:
                    C[row][col] = "."

    ans = 0
    for row in range(H):
        for col in range(W):
            if C[row][col] != ".":
                ans += 1

    return ans


N_ALPHABET: int = 5  # ord("z") - ord("a") + 1


def alf_to_i(c: str) -> int:
    return ord(c) - ord("a")


def i_to_alf(i: int) -> str:
    return chr(ord("a") + i)


def magical_cookies(H, W, C):
    row_colors = [[0] * N_ALPHABET for _ in range(H)]
    col_colors = [[0] * N_ALPHABET for _ in range(W)]

    for row in range(H):
        for col in range(W):
            row_colors[row][alf_to_i(C[row][col])] += 1
            col_colors[col][alf_to_i(C[row][col])] += 1

    cur_height = H
    cur_width = W

    deleted = True
    while deleted:
        deleted = False

        row_to_del = [-1] * H
        for row in range(H):
            for color in range(N_ALPHABET):
                if row_colors[row][color] == cur_width and cur_width >= 2:
                    row_to_del[row] = color
                    deleted = True

        col_to_del = [-1] * W
        for col in range(W):
            for color in range(N_ALPHABET):
                if col_colors[col][color] == cur_height and cur_height >= 2:
                    col_to_del[col] = color
                    deleted = True

        for row in range(H):
            if row_to_del[row] != -1:
                row_colors[row][row_to_del[row]] = 0
                cur_height -= 1
                for col in range(W):
                    col_colors[col][row_to_del[row]] -= 1

        for col in range(W):
            if col_to_del[col] != -1:
                col_colors[col][col_to_del[col]] = 0
                cur_width -= 1
                for row in range(H):
                    row_colors[row][col_to_del[col]] -= 1

    return cur_height * cur_width


def resolve():
    H, W = [int(e) for e in sys.stdin.readline().split()]
    C = [list(sys.stdin.readline().strip()) for _ in range(H)]
    print(magical_cookies(H, W, C))


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
        input = """4 3
aaa
aaa
abc
abd"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5
aaaaa
abcde"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 3
aaa
aaa
aaa"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
