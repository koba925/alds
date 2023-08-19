# 7_A.py

class Tree:

    ROOT_ID = -1
    
    class Node:
        
        def __init__(self, id):
            self.id = id
            self.child = None
            self.sibling = None
            self.parent = None
            self.depth = None

        def type(self):
            return "root" if self.parent is None else "leaf" if self.child is None else "internal node"

        def children(self):
            child = self.child
            while child is not None:
                yield child
                child = child.sibling            

        def set_depth(self, d):
            self.depth = d
            for child in self.children():
                child.set_depth(d + 1)
        
        def __str__(self):
            children = []
            for child in self.children():
                children.append(child.id)
            parent = Tree.ROOT_ID if self.parent is None else self.parent.id 
            return f"node {self.id}: parent = {parent}, depth = {self.depth}, {self.type()}, {children}"

    def __init__(self, size):
        self.size = size
        self.nodes = [Tree.Node(i) for i in range(size)]
        self.root = None

    def id_to_node(self, id):
        return self.nodes[id]

    def nodes_gen(self):
        for id in range(self.size):
            yield self.id_to_node(id)

    def set_parents(self):
        for node in self.nodes_gen():
            for child in node.children():
                child.parent = node

    def set_root(self):
        for node in self.nodes_gen():
            if node.parent is None:
                self.root = node
                break

    def read(self):
    
        def node_read():
            id, k, *child_ids = [int(e) for e in input().split()]
            for i in range(k):
                child = self.id_to_node(child_ids[i])
                if i == 0:
                    self.id_to_node(id).child = child
                else:
                    left_sibling.sibling = child
                left_sibling = child

        for _ in range(self.size):
            node_read()
        self.set_parents()
        self.set_root()
        self.root.set_depth(0)

    def print(self):
        for node in self.nodes_gen():
            print(node)

n = int(input())

T = Tree(n)
T.read()
T.print()
