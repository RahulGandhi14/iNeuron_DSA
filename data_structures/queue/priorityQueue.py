# USING LINKED LIST
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next: Node | None = None


class PriorityQueue:
    def __init__(self):
        self.head: Node | None = None

    def push(self, data, priority):
        node = Node(data, priority)

        if self.head is None:
            self.head = node
        elif self.head.priority < node.priority:
            node.next = self.head
            self.head = node
        else:
            curr = self.head
            while curr.next is not None and curr.next.priority > node.priority:
                curr = curr.next

            node.next = curr.next
            curr.next = node

    def pop(self):
        if self.head is None:
            print("Underflow!!!")
        else:
            curr = self.head
            self.head = self.head.next
            print(curr)
            del curr

    def peek(self):
        if self.head is None:
            print("Underflow!!!")
        else:
            print(self.head)

    def print(self):
        if self.head is None:
            print("EMPTY LIST")
        else:
            curr = self.head
            while curr is not None:
                print("Data:", curr.data, "Priority:", curr.priority, end=" -> ")
                curr = curr.next


llist = PriorityQueue()
llist.push("FIRST", 3)
llist.push("SECOND", 4)
llist.push("THIRD", 2)
llist.push("FORTH", 5)
llist.push("FIFTH", 1)
llist.print()
llist.pop()
llist.print()
llist.peek()
