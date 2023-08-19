# 7_C.py

class Tree:

    class Node:
        def __init__(self):
            self.k = None
            self.l = None
            self.r = None
            self.p = None

    def __init__(self, n) -> None:
        self.nodes = [Tree.Node() for _ in range(n)]
        for _ in range(n):
            k, l, r = [int(e) for e in input().split()]
            self.nodes[k].k = k
            self.nodes[k].l = l
            self.nodes[k].r = r
            if l != -1:
                self.nodes[l].p = k
            if r != -1:
                self.nodes[r].p = k
        for i in range(n):
            if self.nodes[i].p is None:
                self.root = i
                break

    def preorder(self):
        def walk(k):
            yield self.nodes[k]
            if self.nodes[k].l != -1:
                yield from walk(self.nodes[k].l)
            if self.nodes[k].r != -1:
                yield from walk(self.nodes[k].r)
        yield from walk(self.root)

    def inorder(self):
        def walk(k):
            if self.nodes[k].l != -1:
                yield from walk(self.nodes[k].l)
            yield self.nodes[k]
            if self.nodes[k].r != -1:
                yield from walk(self.nodes[k].r)
        yield from walk(self.root)

    def postorder(self):
        def walk(k):
            if self.nodes[k].l != -1:
                yield from walk(self.nodes[k].l)
            if self.nodes[k].r != -1:
                yield from walk(self.nodes[k].r)
            yield self.nodes[k]
        yield from walk(self.root)


n = int(input())
T = Tree(n)

print("Preorder")
for n in T.preorder():
    print(f" {n.k}", end="")
print()

print("Inorder")
for n in T.inorder():
    print(f" {n.k}", end="")
print()

print("Postorder")
for n in T.postorder():
    print(f" {n.k}", end="")
print()
