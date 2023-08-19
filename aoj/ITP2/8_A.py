# 8_A.py Map: Search

from typing import Dict

def insert(map: Dict[str, int], key: str, x: int) -> None:
    map[key] = x

def get(map: Dict[str, int], key: str) -> int:
    return map[key]

from sys import stdin

q = int(stdin.readline())
map: Dict[str, int] = {}
for query in stdin.readlines():
    com, *param = query.split()
    if com == "0":
        insert(map, param[0], int(param[1]))
    elif com == "1":
        print(get(map, param[0]))
