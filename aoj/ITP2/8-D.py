# 8-D.py Multi-Map

from typing import Dict, List, Tuple
from bisect import bisect_left, bisect_right

# TLE #21 0.43s #17 3.78s #15 3.31s #13 3.36s #12 2.29s
class ListMap:

    def __init__(self) -> None:
        self.map: List[Tuple[str, List[int]]] = []
        self.keys: List[str] = []

    def exists(self, p: int, key: str) -> bool:
        return p < len(self.keys) and self.keys[p] == key

    def insert(self, key: str, x: int) -> None:
        p = bisect_left(self.keys, key)
        if self.exists(p, key):
            self.map[p][1].append(x)
        else:
            self.map.insert(p, (key, [x]))
            self.keys.insert(p, key)

    def get(self, key: str) -> None:
        p = bisect_left(self.keys, key)
        if self.exists(p, key):
            for v in self.map[p][1]:
                print(v)

    def delete(self, key: str) -> None:
        p = bisect_left(self.keys, key)
        if self.exists(p, key):
            del self.map[p]
            del self.keys[p]

    def dump(self, left: str, right: str) -> None:
        lp = bisect_left(self.keys, left)
        rp = bisect_right(self.keys, right)
        for k, vs in self.map[lp:rp]:
            for v in vs:
                print(k, v)

# AC #21 04.05s #17 0.77s #15 0.88s #13 1.13s #12 0.85s
class DictMap:

    def __init__(self) -> None:
        self.map: Dict[str, List[int]] = {}

    def insert(self, key: str, x: int) -> None:
        if key in self.map:
            self.map[key].append(x)
        else:
            self.map[key] = [x]

    def get(self, key: str) -> None:
        if key in self.map:
            print(*self.map[key], sep="\n")

    def delete(self, key: str) -> None:
        if key in self.map:
            del self.map[key]

    def dump(self, left: str, right: str) -> None:
        keys = sorted(self.map.keys())
        lp = bisect_left(keys, left)
        rp = bisect_right(keys, right)
        for k in keys[lp:rp]:
            for v in self.map[k]:
                print(k, v)

from sys import stdin

q = int(stdin.readline())

map = ListMap()

for query in stdin.readlines():
    com, *param = query.split()
    if com == "0":
        map.insert(param[0], int(param[1]))
    elif com == "1":
        map.get(param[0])
    elif com == "2":
        map.delete(param[0])
    elif com == "3":
        map.dump(param[0], param[1])