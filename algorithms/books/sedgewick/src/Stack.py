class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def size(self):
         return len(self.items)

     def __iter__(self):
        return iter(reversed(self.items))

if __name__ == "__main__":
    stack = Stack()
    stack.push("foo")
    stack.push("bar")
    stack.push("baz")
    stack.pop()
    for item in stack:
        print(item)
