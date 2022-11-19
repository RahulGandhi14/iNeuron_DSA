from collections import deque


class MyStack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("Peek", stack.peek())
    top = stack.pop()
    print("Top", top)
    print("Peek", stack.peek())
    stack.push(5)
    print("Peek", stack.peek())
