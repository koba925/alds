# 普通は list を使えばよい
s = []
s.append(1) # push
s.pop() # pop

# 自分で書くと

class StackError(Exception):
    def __init__(self,  *args):
        super().__init__(*args)

class Stack:

    MAX_ELEMENT = 100

    def __init__(self):
        self.s = [None] * Stack.MAX_ELEMENT
        self.top = 0

    def push(self, e):
        if self.top >= Stack.MAX_ELEMENT:
            raise StackError("Stack Overflow")
        self.s[self.top] = e
        self.top += 1

    def pop(self):
        if self.top <= 0:
            raise StackError("Stack Underflow")
        self.top -= 1
        return self.s[self.top]
