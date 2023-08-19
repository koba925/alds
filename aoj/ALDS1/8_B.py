# 8_B.py

from sys import stdin


class BinarySearchTree():
    class Node():
        def __init__(self, val, parent, left=None, right=None):
            self.parent = parent
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, val):
        parent = None
        node = self.root

        while node is not None:
            parent = node
            if val < node.val:
                node = node.left
            else:
                node = node.right

        node = BinarySearchTree.Node(val, parent)
        if parent is None:
            self.root = node
        elif val < parent.val:
            parent.left = node
        else:
            parent.right = node

    def find(self, val):
        def rec(node):
            if node is None:
                return False
            if node.val == val:
                return True
            if val < node.val:
                return rec(node.left)
            else:
                return rec(node.right)

        return rec(self.root)

    def walk(self, order):
        def rec(node):
            if order == "pre":
                yield node.val
            if node.left is not None:
                yield from rec(node.left)
            if order == "in":
                yield node.val
            if node.right is not None:
                yield from rec(node.right)
            if order == "post":
                yield node.val

        yield from rec(self.root)

    def to_string(self, order):
        return " ".join(str(e) for e in self.walk(order))

T = BinarySearchTree()
n = int(stdin.readline())

for command in [e.split() for e in stdin.readlines()]:
    if command[0] == "insert":
        T.insert(int(command[1]))
    elif command[0] == "print":
        print(" " + T.to_string("in"))
        print(" " + T.to_string("pre"))
    elif command[0] == "find":
        print("yes" if T.find(int(command[1])) else "no")
