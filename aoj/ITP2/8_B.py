# 8_B.py Map: Search

from collections import defaultdict
from typing import DefaultDict

# dict+getdefault 0.49s 55456KB
# DefaultDict 0.49s 55456KB

def insert(map: DefaultDict[str, int], key: str, x: int) -> None:
    map[key] = x

def get(map: DefaultDict[str, int], key: str) -> int:
    return map[key]

def delete(map: DefaultDict[str, int], key: str) -> None:
    if key in map:
        del map[key]

from sys import stdin

q = int(stdin.readline())
map: DefaultDict[str, int] = defaultdict(int)
for query in stdin.readlines():
    com, *param = query.split()
    if com == "0":
        insert(map, param[0], int(param[1]))
    elif com == "1":
        print(get(map, param[0]))
    elif com == "2":
        delete(map, param[0])
