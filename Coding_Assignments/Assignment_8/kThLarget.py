import heapq


def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(findKthLargest(nums, 4)[-1])
