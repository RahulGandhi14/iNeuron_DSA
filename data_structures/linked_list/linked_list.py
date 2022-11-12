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

        while current:
            right = current.next
            current.next = left
            left = current
            current = right

        self.head = left

    def detectCycle(self):
        slower = self.head
        faster = None if self.head is None else self.head.next

        while faster != slower and (faster is not None and slower is not None):
            slower = slower.next
            faster = None if faster.next is None else faster.next.next

        if faster == slower and self.head is not None:
            return True
        else:
            return False

    def deleteNodeAtPos(self, idx):
        if self.head is None:
            return

        curr = self.head

        if idx == 0:
            self.head = self.head.next
        else:
            for i in range(idx - 1):
                curr = curr.next
                if curr is None:
                    return

            tempPtr = curr.next.next
            curr.next = tempPtr
            del tempPtr

    def count(self):
        numOfNodes = 0
        curr = self.head
        while curr is not None:
            numOfNodes += 1
            curr = curr.next

        return numOfNodes

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
print("Number of Nodes:", llist.count())

# Create cycle
# llist.add(6, True)

doesCycleExist = llist.detectCycle()

if not doesCycleExist:
    print("Does cycle exist?", "Yes" if doesCycleExist else "No")
    if llist.head is not None:
        llist.display()
        # llist.reverse()
        llist.deleteNodeAtPos(4)
        print("Number of Nodes:", llist.count())
        llist.display()
else:
    print("Does cycle exist?", "Yes" if doesCycleExist else "No")
