import heapq


def findKthSmallest(nums, k):
    return heapq.nsmallest(k, nums)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
print(findKthSmallest(nums, 4)[-1])
