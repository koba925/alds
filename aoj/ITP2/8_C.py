# 8_C.py Map: Search

# use sorted list AC 07.40 s 60280 KB
# use dict #20 16.99s(TLE) 

from typing import Dict, List, Tuple
from bisect import bisect_left, bisect_right

class ListMap:

    def __init__(self) -> None:
        self.map: List[Tuple[str, int]] = []
        self.keys: List[str] = []

    def exists(self, p: int, key: str) -> bool:
        return p < len(self.keys) and self.keys[p] == key

    def insert(self, key: str, x: int) -> None:
        p = bisect_left(self.keys, key)
        if self.exists(p, key):
            self.map[p] = (key, x)
        else:
            self.map.insert(p, (key, x))
            self.keys.insert(p, key)

    def get(self, key: str) -> None:
        p = bisect_left(self.keys, key)
        print(self.map[p][1] if self.exists(p, key) else 0)

    def delete(self, key: str) -> None:
        p = bisect_left(self.keys, key)
        if self.exists(p, key):
            del self.map[p]
            del self.keys[p]

    def dump(self, left: str, right: str) -> None:
        lp = bisect_left(self.keys, left)
        rp = bisect_right(self.keys, right)
        for k, v in self.map[lp:rp]:
            print(k, v)

class DictMap:

    def __init__(self) -> None:
        self.map: Dict[str, int] = {}

    def insert(self, key: str, x: int) -> None:
        self.map[key] = x

    def get(self, key: str) -> None:
        print(self.map[key] if key in self.map else 0)

    def delete(self, key: str) -> None:
        if key in self.map:
            del self.map[key]

    def dump(self, left: str, right: str) -> None:
        keys = sorted(self.map.keys())
        lp = bisect_left(keys, left)
        rp = bisect_right(keys, right)
        # Faster, but still too slow
        if lp < rp:
            print("\n".join([f"{k} {self.map[k]}" for k in keys[lp:rp]]))
        # for k in keys[lp:rp]:
        #     print(k, self.map[k])

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
