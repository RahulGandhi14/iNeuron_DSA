import heapq


## Approach 1
# def findKthLargest(nums, k):
#     return heapq.nlargest(k, nums)


# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# print("Approach 1:", findKthLargest(nums, 4)[-1])


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


## Approach 2
def findKthLargestElement(nums, k):
    return selectionProcedure(nums, 0, len(nums) - 1, len(nums) - k)


arr = [40, 25, 68, 79, 52, 66, 89, 97]
k = 2
print("Approach 2:", findKthLargestElement(arr, k))
