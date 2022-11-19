# https://leetcode.com/problems/palindrome-linked-list/
"""
Time And Space Complexity: O(n)
"""

# We can also solve using Stack.


def isPalindrome1(self, head):
    arr = list()
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    start = 0
    end = len(arr) - 1
    isPalindrome = True
    while start <= end:
        if arr[start] != arr[end]:
            isPalindrome = False
            break
        else:
            start += 1
            end -= 1

    return isPalindrome


"""
# Using Recursion
Time And Space Complexity: O(n)
"""


def isPalindromeUsingRecursion(self, head):
    self.front = head

    def recursive_check(current):
        if current:
            if not recursive_check(current.next):
                return False
            if current.val != self.front.val:
                return False
            self.front = self.front.next
        return True

    return recursive_check(head)


"""
Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def isPalindrome(self, head):
        if head is None:
            return True

        # Two runners pointer technique
        # Fast runner moves down 2 nodes
        # while slow runner just 1.
        # By the time fast runner reaches to end
        # Slower would be half way through.
        first_half_end = self.get_end_of_first_half(head)
        reversed_second_half_head = self.reverse(first_half_end.next)
        curr = head
        result = True

        while reversed_second_half_head and result:
            if curr.val != reversed_second_half_head.val:
                result = False
            curr = curr.next
            reversed_second_half_head = reversed_second_half_head.next

        first_half_end.next = self.reverse(reversed_second_half_head)
        return result

    def get_end_of_first_half(self, head):
        faster = head
        slower = head
        while faster.next and faster.next.next:
            faster = faster.next.next
            slower = slower.next
        return slower

    def reverse(self, head):
        curr = head
        prevPtr = None
        nextPtr = None

        while curr:
            nextPtr = curr.next
            curr.next = prevPtr
            prevPtr = curr
            curr = nextPtr
        return prevPtr
