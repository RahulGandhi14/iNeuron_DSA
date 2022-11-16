from ...data_structures.linked_list.linked_list import LinkedList, Node


def display(head):
    curr = head
    while curr:
        print(curr.value, end="->")
        curr = curr.next


def segregate(head):
    # https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
    # Head Pointers
    zeros = Node()
    ones = Node()
    twos = Node()

    # End(right) Pointers - Will be at last node
    zero = zeros
    one = ones
    two = twos

    curr = head
    while curr:
        if curr.value == 0:
            zero.next = curr
            zero = zero.next
        elif curr.value == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next

        curr = curr.next

    newHead = zeros.next if zeros.next else ones.next if ones.next else twos.next
    zero.next = ones.next if ones.next else twos.next
    one.next = twos.next
    two.next = None

    return newHead


llist = LinkedList()
for item in [2, 1, 2, 1]:
    llist.add(item)
newHead = segregate(llist.head)
display(newHead)
