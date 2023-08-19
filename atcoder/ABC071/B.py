import sys

def resolve_set():
    S = sys.stdin.readline().strip()
    used = set(S)
    notused = set("abcdefghijklmnopqrstuvwxyz") - used
    word = sorted(list(notused))[0] if len(notused) > 0 else "None"
    print(word)

N_ALPHABET: int = ord("z") - ord("a") + 1
def alf_to_i(c: str) -> int: return ord(c) - ord("a")
def i_to_alf(i: int) -> str: return chr(ord("a") + i)

def resolve():
    S = sys.stdin.readline().strip()
    used = [False] * N_ALPHABET
    for c in S:
        used[alf_to_i(c)] = True
    for i, u in enumerate(used):
        if not u:
            print(i_to_alf(i))
            break
    else:
        print("None")

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
        input = """atcoderregularcontest"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcdefghijklmnopqrstuvwxyz"""
        output = """None"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg"""
        output = """d"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
