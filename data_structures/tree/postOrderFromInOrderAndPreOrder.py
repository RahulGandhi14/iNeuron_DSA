def postOrder(inOrder, preOrder, inStart, inEnd, hashMap):
    if inStart > inEnd:
        return

    inIndex = hashMap[preOrder[postOrder.preIndex]]
    postOrder.preIndex += 1

    # PRINT LEFT SUBTREE
    postOrder(inOrder, preOrder, inStart, inIndex - 1, hashMap)
    # PRINT RIGHT SUBTREE
    postOrder(inOrder, preOrder, inIndex + 1, inEnd, hashMap)

    print(inOrder[inIndex], end="  ")


def postOrderWrapper(inOrder, preOrder):
    lenOfInOrder = len(inOrder)
    hashMap = dict()

    for i in range(lenOfInOrder):
        hashMap[inOrder[i]] = i

    postOrder.preIndex = 0
    postOrder(inOrder, preOrder, 0, lenOfInOrder - 1, hashMap)


# Driver program to test above function
inOrder = ["D", "B", "E", "A", "F", "C"]
preOrder = ["A", "B", "D", "E", "C", "F"]
postOrderWrapper(inOrder, preOrder)
print("\n")
