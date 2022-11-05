import heapq

## Approach 1: Using Heap
def findKthSmallest(nums, k):
    return heapq.nsmallest(k, nums)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print("Approach 1:", findKthSmallest(nums, 4)[-1])
arr = [40, 25, 68, 79, 52, 66, 89, 97, 39]
print("Approach 1:", findKthSmallest(arr, 3)[-1])


## Approach 2: Using Quick Sort Partition Method


def partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(p + 1, q + 1):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[p] = arr[p], arr[i]
    return i


def selectionProcedure(arr, p, q, k):
    idx = partition(arr, p, q)
    if idx == k:
        return arr[idx]
    elif k < idx:
        return selectionProcedure(arr, p, idx - 1, k)
    else:
        return selectionProcedure(arr, idx + 1, q, k)


def findKthMinElement(arr, k):
    return selectionProcedure(arr, 0, len(arr) - 1, k)


arr = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print("Approach 2:", findKthMinElement(arr, k - 1))
arr = [40, 25, 68, 79, 52, 66, 89, 97, 39]
k = 3
print("Approach 2(Arr 2):", findKthMinElement(arr, k - 1))
