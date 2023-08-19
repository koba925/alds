# 4_C.py

import sys

class Dictionary:
    def __init__(self) -> None:
        self.dic = set()
    
    def insert(self, string):
        self.dic.add(string)
    
    def find(self, string):
        return string in self.dic        

n = int(sys.__stdin__.readline())

dic = Dictionary()

for _ in range(n):
    command, string = sys.__stdin__.readline().split()
    if command == "insert":
        dic.insert(string)
    elif command == "find":
        print("yes" if dic.find(string) else "no")
