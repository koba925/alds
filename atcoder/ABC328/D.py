def resolve_contest():
    S = input()

    L = []
    for s in S:
        L.append(s)
        if len(L) >= 3 and L[-3:] == ["A", "B", "C"]:
            # L.pop(); L.pop(); L.pop()
            # del L[-3:]
            L = L[:-3] # TLE
    print("".join(L))

class DoublyLinkedList:

    class Node:
        def __init__(self, val = None, prev = None, next = None):
            self.prev = prev
            self.next = next
            self.val = val
        
        def __repr__(self):
            return str(self.val)

    def __init__(self):
        self.end = DoublyLinkedList.Node(None)
        self.end.next = self.end  # head
        self.end.prev = self.end  # tail
        self.cursor = self.end

    def head(self):
        return self.end.next
    
    def tail(self):
        return self.end.prev
    
    def insert_before(self, node, val):
        new_node = DoublyLinkedList.Node(val, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node
        return new_node

    def insert_after(self, node, val):
        new_node = DoublyLinkedList.Node(val, node, node.next)
        node.next.prev = new_node
        node.next = new_node
        return new_node

    def insert_before_cursor(self, val):
        self.cursor = self.insert_before(self.cursor, val)

    def insert_after_cursor(self, val):
        self.cursor = self.insert_before(self.cursor, val)
    
    def unlink(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def unlink_at_cursor(self):
        cursor = self.cursor.next
        self.unlink(self.cursor)
        self.cursor = cursor

    def move_cursor(self, n):
        if n > 0:
            for _ in range(n):
                self.cursor = self.cursor.next
        else:
            for _ in range(-n):
                self.cursor = self.cursor.prev

    def push_head(self, val):
        self.insert_after(self.end, val)
        
    def push_tail(self, val):
        self.insert_before(self.end, val)

    def pop_head(self):
        val = self.end.next.val
        self.unlink(self.end.next)
        return val

    def pop_tail(self):
        val = self.end.prev.val
        self.unlink(self.end.prev)
        return val

    def find_by_val(self, val):
        node = self.end.next
        while node != self.end:
            if node.val == val:
                return node
            node = node.next
        return None
    
    def delete_by_val(self, val):
        node = self.find_by_val(val)
        if node != None:
            self.unlink(node)
    
    def vals(self):
        node = self.end.next
        while node != self.end:
            yield node.val
            node = node.next

def resolve():
    def prev_val(node):
        return node.prev.val if node.prev != L.end else ""
    
    def prev_prev_val(node):
        return node.prev.prev.val if node.prev != L.end and node.prev.prev != L.end else ""
    
    S = input()

    L = DoublyLinkedList()
    for s in S:
        L.push_tail(s)
    
    node = L.head()
    while node != L.end:
        abc = prev_prev_val(node) + prev_val(node) + node.val
        node = node.next
        if abc == "ABC":
            L.unlink(node.prev)
            L.unlink(node.prev)
            L.unlink(node.prev)
    
    print("".join(L.vals()))

# resolve()
# exit()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """BAABCBCCABCAC"""
        output = """BCAC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ABCABC"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """AAABCABCABCAABCABCBBBAABCBCCCAAABCBCBCC"""
        output = """AAABBBCCC"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
