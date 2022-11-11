class Node:
    def __init__(self, value):
        self.value = value
        self.next: None | Node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = node

    def reverse(self):
        left = None
        current = self.head
        right = self.head

        while right is not None:
            right = current.next
            current.next = left
            left = current
            current = right

        self.head = left

    def display(self):
        current = self.head
        while current is not None:
            print(current.value, end="-->")
            current = current.next
        print(end="\n")


llist = LinkedList()
llist.add(1)
llist.add(2)
llist.add(3)
llist.add(4)
llist.add(5)
llist.display()
llist.reverse()
llist.display()
