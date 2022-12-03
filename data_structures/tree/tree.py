from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


# PreOrder
def preOrder(root: Node):
    if root:
        print(root.data, " ", end=" ")
        preOrder(root.left)
        preOrder(root.right)


def inOrder(root: Node):
    if root:
        inOrder(root.left)
        print(root.data, " ", end=" ")
        inOrder(root.right)


def postOrder(root: Node):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, " ", end=" ")


## ITERATIVE APPROACHs
def preOrderIterative(root: Node):
    stack = deque()
    stack.append(root)

    while len(stack) != 0:
        element = stack.pop()
        print(element.data, " ", end=" ")
        if element.right:
            stack.append(element.right)
        if element.left:
            stack.append(element.left)


def inOrderIterative(root: Node):
    curr = root
    stack = deque()

    while curr or len(stack) != 0:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        print(curr.data, " ", end=" ")

        curr = curr.right


def postOrderIterative(root: Node):
    curr = root
    stack = deque()

    while curr or len(stack) != 0:
        while curr:
            if curr.right:
                stack.append(curr.right)
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        if curr.right and len(stack) != 0 and curr.right == stack[-1]:
            stack.pop()
            stack.append(curr)
            curr = curr.right
        else:
            print(curr.data, " ", end=" ")
            curr = None


# Driver Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("PRE ORDER:", end=" ")
preOrder(root)
print(end="\n")

print("PRE ORDER ITERATIVE:", end=" ")
preOrderIterative(root)
print(end="\n")

print("IN ORDER:", end=" ")
inOrder(root)
print(end="\n")

print("IN ORDER ITERATIVE:", end=" ")
inOrderIterative(root)
print(end="\n")

print("POST ORDER:", end=" ")
postOrder(root)
print(end="\n")

print("POST ORDER ITERATIVE:", end=" ")
postOrderIterative(root)
print(end="\n")
