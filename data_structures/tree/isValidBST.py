from tree import Node


def isValidBST(root: Node) -> bool:
    stack = list()
    curr = root
    pre = None

    while curr or len(stack) != 0:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        if pre and pre.val >= curr.val:
            return False

        pre = curr
        curr = curr.right

    return True
