# 3_A.py

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
        

def operate_binary(stack, op):
    b = stack.pop()
    a = stack.pop()
    stack.push(op(a, b))

terms = input().split()

stack = Stack()
for t in terms:
    if t == "*":
        operate_binary(stack, lambda a, b: a * b)
    elif t == "+":
        operate_binary(stack, lambda a, b: a + b)
    elif t == "-":
        operate_binary(stack, lambda a, b: a - b)
    else:
        stack.push(int(t))

print(stack.pop())

