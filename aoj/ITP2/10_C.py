# 10_C.py Bit Operation II

from sys import stdin
from typing import List, Callable, Optional


class Bits:

    def __init__(self, len: int) -> None:
        self.length = len
        self.mask = 2 ** len - 1
        self.bits: int = 0

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


q = int(stdin.readline())
flags = Bits(64)
funcs: List[Callable[..., Optional[int]]] = [
    flags.test, flags.set, flags.clear, flags.flip,
    flags.all, flags.any, flags.none, flags.count, flags.val
]

for line in stdin.readlines():
    com, *param = [int(e) for e in line.split()]
    ret = funcs[com](*param)
    if ret is not None:
        print(ret)
    # print(flags)
