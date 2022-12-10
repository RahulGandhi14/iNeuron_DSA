from tree import Node, postOrder


def buildTree(inOrder, preOrder, inStart, inEnd, hashMap):
    if inStart > inEnd:
        return None

    node = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    if inStart == inEnd:
        return node

    inIndex = hashMap[node.data]
    node.left = buildTree(inOrder, preOrder, inStart, inIndex - 1, hashMap)
    node.right = buildTree(inOrder, preOrder, inIndex + 1, inEnd, hashMap)

    return node


def buildTreeWrap(inOrder, preOrder, lenOfInOrder):
    hashMap = dict()

    for i in range(lenOfInOrder):
        hashMap[inOrder[i]] = i

    # Static variable preIndex
    buildTree.preIndex = 0
    return buildTree(inOrder, preOrder, 0, lenOfInOrder - 1, hashMap)


# Driver program to test above function
inOrder = ["D", "B", "E", "A", "F", "C"]
preOrder = ["A", "B", "D", "E", "C", "F"]

root = buildTreeWrap(inOrder, preOrder, len(inOrder))

# POST ORDER TRAVERSAL
postOrder(root)
print("\n")
