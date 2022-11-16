# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


def removeNthFromEnd(head, n):
    start = Node()
    slow = start
    fast = start
    slow.next = head

    while n > 0:
        fast = fast.next
        n -= 1

    while fast and fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return start.next


def Appraoch2(head, n):
    slower = head
    faster = head

    temp = n
    while temp > 0:
        faster = faster.next
        temp -= 1

    while faster and faster.next:
        faster = faster.next
        slower = slower.next

    if faster is None and slower == head:
        head = head.next
    else:
        slower.next = slower.next.next if slower.next else slower.next

    return head


def removeNthFromEndBruteForce(head, n):
    total = 0
    curr = head
    while curr:
        total += 1
        curr = curr.next

    if total - n == 0:
        head = head.next
        return head

    idx = 0
    curr = head
    while idx < total - n - 1:
        idx += 1
        curr = curr.next

    if idx == 0 and curr.next is None:
        return head.next

    if curr and curr.next:
        curr.next = curr.next.next
        if idx == 0:
            head = curr

    return head
