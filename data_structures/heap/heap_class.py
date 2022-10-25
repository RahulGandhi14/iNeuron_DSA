class heap:
    def __init__(self, arr):
        self.heapArr = arr
        self.buildHeap()

    def buildHeap(self):
        for i in range((len(self.heapArr) // 2), -1, -1):
            self.heapify(len(self.heapArr), i)

    def heapify(self, n, idx):
        leftChildIdx = 2 * idx + 1
        rightChildIdx = 2 * idx + 2

        largest = self.getLargest(idx, leftChildIdx, rightChildIdx, n)

        if self.heapArr[largest] > self.heapArr[idx]:
            self.swap(largest, idx)
            self.heapify(n, idx)

    def pop(self):
        element = self.peek()
        self.swap(0, len(self.heapArr) - 1)
        del self.heapArr[len(self.heapArr) - 1]
        self.buildHeap()
        return element

    def peek(self):
        return self.heapArr[0]

    def insert(self, element):
        self.heapArr.append(element)
        self.buildHeap()

    def printArr(self):
        print(self.heapArr)

    def swap(self, i, j):
        self.heapArr[i], self.heapArr[j] = self.heapArr[j], self.heapArr[i]

    def getLargest(self, idx, leftChildIdx, rightChildIdx, n):
        largest = idx
        if rightChildIdx < n and self.heapArr[rightChildIdx] > self.heapArr[largest]:
            largest = rightChildIdx
        if leftChildIdx < n and self.heapArr[leftChildIdx] > self.heapArr[largest]:
            largest = leftChildIdx
        return largest


# K Largest
nums = [3, 2, 1, 5, 6, 4]
heapArr = heap(nums)

k = 2
largest = None
for i in range(k):
    largest = heapArr.pop()

print(largest)


# K Smallest
# heapArr = heap([n * -1 for n in nums])
# heapArr.printArr()

# k = 2
# for i in range(k - 1):
#     heapArr.pop()

# print(heapArr.peek() * -1)
