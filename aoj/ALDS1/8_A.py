# 8_A.py

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

    def reduce(self, order, func, init=0):
        def rec(node):
            nonlocal acc
            if order == "pre":
                acc = func(acc, node.val)
            if node.left is not None:
                rec(node.left)
            if order == "in":
                acc = func(acc, node.val)
            if node.right is not None:
                rec(node.right)
            if order == "post":
                acc = func(acc, node.val)
            return acc

        acc = init
        return rec(self.root)

def to_string(tree, order):
    return T.reduce(order, lambda acc, e: acc + f" {e}", "")

from sys import stdin

T = BinarySearchTree()
n = int(stdin.readline())

for command in [e.split() for e in stdin.readlines()]:
    if command[0] == "insert":
        T.insert(int(command[1]))
    elif command[0] == "print":
        print(to_string(T, "in"))
        print(to_string(T, "pre"))
