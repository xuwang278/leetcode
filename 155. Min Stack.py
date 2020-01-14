class Stack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 
        self._stack = [] 
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if self._stack:
            x = (x, self._stack[-1])
        self._stack.append(x)

    def pop(self) -> None:
        self.stack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get(self) -> int:
        return self._stack[-1]

print(123)

# Your Stack object will be instantiated and called as such:
# obj = Stack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get()