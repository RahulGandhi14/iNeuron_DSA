class Node:
    def __init__(self, value):
        self.value = value
        self.next: None | Node = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value, createCycle=False):
        node = Node(value)

        # Creating cycle
        if createCycle:
            if value == 5:
                node.next = self.head

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

    def detectCycle(self):
        slower = self.head
        faster = self.head.next

        while faster != slower and (faster is not None and slower is not None):
            slower = slower.next
            faster = faster.next.next

        if faster == slower:
            return True
        else:
            return False

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

# Create cycle
# llist.add(6, True)

doesCycleExist = llist.detectCycle()
if not doesCycleExist:

    llist.display()
    llist.reverse()
    llist.display()
else:
    print("Does cycle exist?", "Yes" if doesCycleExist else "No")
