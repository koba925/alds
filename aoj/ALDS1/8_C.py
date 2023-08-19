# 8_C.py

from sys import stdin


class BinarySearchTree():
    class Node():
        def __init__(self, key, parent, left=None, right=None):
            self.parent = parent
            self.key = key
            self.left = left
            self.right = right

        def __repr__(self) -> str:
            p = self.parent and self.parent.key
            l = self.left and self.left.key
            r = self.right and self.right.key
            return f"<v:{self.key} p:{p} l:{l} r:{r}>"

    def __init__(self):
        self.root = None

    def insert(self, key):
        parent = None
        node = self.root

        while node is not None:
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        node = BinarySearchTree.Node(key, parent)
        if parent is None:
            self.root = node
        elif key < parent.key:
            parent.left = node
        else:
            parent.right = node

    def find_node(self, key):
        def rec(node):
            if node is None:
                return None
            if node.key == key:
                return node
            if key < node.key:
                return rec(node.left)
            else:
                return rec(node.right)

        return rec(self.root)

    def contains(self, key):
        return self.find_node(key) != None

    def delete_node(self, node):
        def successor(node):
            def minimum(node):
                return node if node.left is None else minimum(node.left)
            return minimum(node.right)

        if node.left is None or node.right is None:
            node_to_del = node
        else:
            node_to_del = successor(node)
            node.key = node_to_del.key

        p = node_to_del.parent
        child = node_to_del.left or node_to_del.right
        if child is not None:
            child.parent = p
        if p is None:
            self.root = child
        elif p.left == node_to_del:
            p.left = child
        else:
            p.right = child

    def delete(self, key):
        self.delete_node(self.find_node(key))

    def walk(self, order):
        def rec(node):
            if order == "pre":
                yield node.key
            if node.left is not None:
                yield from rec(node.left)
            if order == "in":
                yield node.key
            if node.right is not None:
                yield from rec(node.right)
            if order == "post":
                yield node.key

        yield from rec(self.root)

    def to_string(self, order):
        return " ".join(str(e) for e in self.walk(order))


T = BinarySearchTree()
n = int(stdin.readline())

for command in [e.split() for e in stdin.readlines()]:
    if command[0] == "insert":
        T.insert(int(command[1]))
    elif command[0] == "delete":
        T.delete(int(command[1]))
    elif command[0] == "find":
        print("yes" if T.contains(int(command[1])) else "no")
    elif command[0] == "print":
        print(" " + T.to_string("in"))
        print(" " + T.to_string("pre"))
