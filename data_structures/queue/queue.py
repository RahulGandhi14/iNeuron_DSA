from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


if __name__ == "__main__":
    queue = MyQueue()
    print("Is Empty:", queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.display()
    print("-->DEQUEUE:", queue.dequeue())
    print("-->Size:", queue.size())
    print("Is Empty:", queue.is_empty())
    queue.display()
