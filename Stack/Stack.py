#This is the basic stack implementation from scratch with outputs.

class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0 #or self.items == []
    
    def peek(self):
        if self.items:
            return self.items[-1]

    def get_stack(self):
        return self.items

s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.pop()
s.push("C")
print(s.get_stack())
print(s.is_empty())
print(s.peek())

#OUTPUT:
['A', 'B']
['A', 'C']
False
C
