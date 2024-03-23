import sys
from io import StringIO
import unittest

def resolve_dictset():
    import collections as cl

    N, Q = int(input()), int(input())

    nums = [[] for _ in range(N)]
    boxes = cl.defaultdict(lambda: set())

    for _ in range(Q):
        c, *p = [int(e) for e in input().split()]
        match c:
            case 1:
                num, box = p
                nums[box - 1].append(num)
                boxes[num].add(box)
            case 2:
                print(*sorted(nums[p[0] - 1]))
            case 3:
                print(*sorted(boxes[p[0]]))

def resolve():
    N, Q = int(input()), int(input())

    nums = [[] for _ in range(N)]
    boxes = [set() for _ in range(2 * 10 ** 6)]

    for _ in range(Q):
        c, *p = [int(e) for e in input().split()]
        match c:
            case 1:
                num, box = p
                nums[box - 1].append(num)
                boxes[num - 1].add(box)
            case 2:
                print(*sorted(nums[p[0] - 1]))
            case 3:
                print(*sorted(boxes[p[0] - 1]))

class TestClass(unittest.TestCase):
    def test_sample1(self):
        input = """5
8
1 1 1
1 2 4
1 1 4
2 4
1 1 4
2 4
3 1
3 2"""
        expected = """1 2
1 1 2
1 4
4"""
        self.assertIO(input, expected)

    def test_sample2(self):
        input = """1
5
1 1 1
1 2 1
1 200000 1
2 1
3 200000"""
        expected = """1 2 200000
1"""
        self.assertIO(input, expected)

    def assertIO(self, input, expected):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        actual = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
