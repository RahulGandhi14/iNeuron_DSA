arr = [1, 3, 7, 9, 12, 10, 8, 16, 18, 22, 27, 0]

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def getSmallest(arr, i, leftIdx, rightIdx, n):
    smallest = i

    if(rightIdx < n and arr[rightIdx] < arr[smallest]):
        smallest = rightIdx
    
    if(leftIdx < n and arr[leftIdx] < arr[smallest]):
        smallest = leftIdx

    return smallest

def heapify(arr, n, i):
    leftChildIdx = 2*i + 1
    rightChildIdx = 2*i + 2

    smallest = getSmallest(arr, i, leftChildIdx, rightChildIdx, n)

    if(arr[smallest] < arr[i]):
        swap(arr, smallest, i)
        heapify(arr, n, smallest)


def buildHeap(arr, n):
    for i in range((n//2)-1, -1, -1):
        heapify(arr, n, i)

def sort(arr):
    for i in range(len(arr)-1,0,-1):
        swap(arr, i, 0)
        heapify(arr, i, 0)

def heapSort(arr):
    buildHeap(arr, len(arr))
    sort(arr)
    print(arr)


heapSort(arr)