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
