def resolve_dict():
    players = {
        "tourist": 3858,
        "ksun48": 3679,
        "Benq": 3658,
        "Um_nik": 3648,
        "apiad": 3638,
        "Stonefeang": 3630,
        "ecnerwala": 3613,
        "mnbvmar": 3555,
        "newbiedmy": 3516,
        "semiexp": 3481,
    }

    print(players[input()])


def resolve():
    players_data = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481"""

    players_dict = {
        name: rate for name, rate in [l.split() for l in players_data.splitlines()]
    }
    print(players_dict[input()])


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
        input = """tourist"""
        output = """3858"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """semiexp"""
        output = """3481"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
