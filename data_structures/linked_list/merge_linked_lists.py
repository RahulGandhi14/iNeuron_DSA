from linked_list import LinkedList, Node

"""
Approach1: Using Merge Combine Procedure
Time Complexity: O(m+n)
Space Complexity: O(m+n)
"""


def MergeTwoSortedLinkedLists(head1: Node, head2: Node):
    llist = LinkedList()

    llist1 = head1
    llist2 = head2

    while llist1 and llist2:
        if llist2.value > llist1.value:
            llist.add(llist1.value)
            llist1 = llist1.next
        else:
            llist.add(llist2.value)
            llist2 = llist2.next

    while llist1:
        llist.add(llist1.value)
        llist1 = llist1.next

    while llist2:
        llist.add(llist2.value)
        llist2 = llist2.next

    llist.display()


"""
Approach2:
Space Complexity: O(m+n)
Stack Space: O(m+n)
"""


def MergeLists(head1: Node, head2: Node):
    temp: Node = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.value < head2.value:
        temp = head1
        temp.next = MergeLists(head1.next, head2)
    else:
        temp = head2
        temp.next = MergeLists(head1, head2.next)

    return temp


if __name__ == "__main__":
    llist1 = LinkedList()
    llist1.add(1)
    llist1.add(3)
    llist1.add(5)
    llist1.add(7)
    llist1.display()

    llist2 = LinkedList()
    llist2.add(2)
    llist2.add(4)
    llist2.add(6)
    llist2.add(8)
    llist2.add(9)
    llist2.display()

    print("Approach1:")
    MergeTwoSortedLinkedLists(llist1.head, llist2.head)

    print("Approach2")
    llist3 = LinkedList()
    llist3.head = MergeLists(llist1.head, llist2.head)
    llist3.display()
