# 15_D.py Huffman Coding

# from __future__ import annotations
from typing import Dict, Optional
from collections import Counter
from heapq import heapify, heappush, heappop


class HuffmanTree:

    class Node:

        def __init__(self, freq: int, c: str, 
                     l: Optional["HuffmanTree.Node"] = None, 
                     r: Optional["HuffmanTree.Node"] = None) -> None:
            self.freq = freq
            self.c = c
            self.l = l
            self.r = r

        def __repr__(self) -> str:
            return (f"Node({self.freq},'{self.c}')")

        def __lt__(self, other: "HuffmanTree.Node") -> bool:
            return self.freq < other.freq

    def __init__(self, source: str) -> None:
        self.text = source
        self.root = self.build_tree()
        self.dict = self.build_dict()

    def build_tree(self) -> "HuffmanTree.Node":
        counts = [HuffmanTree.Node(freq, c)
                  for c, freq in Counter(self.text).items()]
        heapify(counts)
        if len(counts) == 1:
            l = heappop(counts)
            return HuffmanTree.Node(l.freq, "", l, None)
        while len(counts) > 1:
            l = heappop(counts)
            r = heappop(counts)
            heappush(counts, HuffmanTree.Node(l.freq + r.freq, "", l, r))
        return heappop(counts)

    def print_tree(self) -> None:

        def rec(n: "HuffmanTree.Node", prefix: str) -> None:
            print(f"{prefix} : '{n.c}', {n.freq}")
            if n.l is not None:
                rec(n.l, prefix + "0")
            if n.r is not None:
                rec(n.r, prefix + "1")
        
        rec(self.root, "")

    def build_dict(self) -> Dict[str, str]:
        
        def rec(n: HuffmanTree.Node, s: str) -> None:
            if n.c != "":
                d[n.c] = s
            if n.l is not None:
                rec(n.l, s + "0")
            if n.r is not None:
                rec(n.r, s + "1")
        
        d: Dict[str, str] = {}
        rec(self.root, "")
        return d

    def encode(self, text: str) -> str:
        return "".join([self.dict[c] for c in text])

    def decode(self, text: str) -> str:
        decoded = ""
        n: Optional["HuffmanTree.Node"] = self.root
        if n is None:
            return decoded
        for c in text:
            n = n.l if c == "0" else n.r
            if n is None:
                break
            if n.c != "":
                decoded += n.c
                n = self.root
        return decoded

S: str = input()
ht = HuffmanTree(S)
# ht.print_tree()
# print(ht.encode(S))
# print(ht.decode(ht.encode(S)))
print(len(ht.encode(S)))

