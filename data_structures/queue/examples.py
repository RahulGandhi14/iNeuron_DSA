from queue import MyQueue


def produceBinaryNumber(n):
    queue = MyQueue()
    queue.enqueue("1")

    while n:
        n -= 1
        number = int(queue.dequeue())
        print(number, end=" ")
        queue.enqueue(str(number) + "0")
        queue.enqueue(str(number) + "1")

    print(end="\n")


n = 5
print("->BINARY NUMBERS UPTO", n, ":", end=" ")
produceBinaryNumber(5)


# STACK USING QUEUE
class MyStack:
    def __init__(self):
        self.stack = MyQueue()
        self.temp = MyQueue()

    def push(self, x: int) -> None:
        self.stack.enqueue(x)

    def pop(self) -> int:
        size = self.stack.size()

        for _ in range(size - 1):
            self.stack.enqueue(self.stack.dequeue())

        return self.stack.dequeue()

    def top(self) -> int:
        return self.stack.queue[self.stack.size() - 1]

    def empty(self) -> bool:
        print(self.stack.queue)
        return self.stack.is_empty()


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print("TOP", stack.top())
print("POP", stack.pop())
print("is Empty", stack.empty())
stack.push(4)
print("is Empty", stack.empty())
print("POP", stack.pop())
print("is Empty", stack.empty())
