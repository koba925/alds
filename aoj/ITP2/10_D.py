# 10_C.py Bit Operation II

from typing import List, Callable, Optional

class Bits:

    @classmethod
    def calc_mask(cls, masks:List[int]) -> int:
        mask = 0
        for m in masks:
            mask |= 1 << m
        return mask

    def __init__(self, len: int, masks: List[int]) -> None:
        self.length = len
        self.mask = 2 ** len - 1
        self.masks = masks
        self.bits: int = 0

    def __str__(self) -> str:
        return f"{self.bits:0{self.length}b}"

    def __repr__(self) -> str:
        return f"Bits({self.bits:0{self.length}b})"

    def test(self, i: int) -> int:
        return self.bits >> i &  1
    
    def set(self, m: int) -> None:
        self.bits |= self.masks[m]

    def clear(self, m: int)-> None:
        self.bits &= (self.masks[m] ^ self.mask)

    def flip(self, m: int)-> None:
        self.bits ^= self.masks[m]

    def all(self, m: int) -> int:
        m = self.masks[m]
        return 1 if self.bits & m == m else 0

    def any(self, m: int) -> int:
        return 1 if self.bits & self.masks[m] != 0 else 0

    def none(self, m: int) -> int:
        return 1 if self.bits & self.masks[m] == 0 else 0

    def count(self, m: int) -> int:
        bs, c = self.bits & self.masks[m], 0
        for _ in range(self.length):
            c += bs & 1
            bs >>= 1
        return c

    def val(self, m: int) -> int:
        return self.bits & self.masks[m]

from sys import stdin

n = int(stdin.readline())
masks = [Bits.calc_mask(
    [int(e) for e in stdin.readline().split()][1:]
) for _ in range(n)]

q = int(stdin.readline())
flags = Bits(64, masks)
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
