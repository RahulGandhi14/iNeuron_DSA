# https://leetcode.com/problems/find-peak-element/


# Approach 1
# O(n)
def findPeakElementLinear(nums):
    for i in range(len(nums)):
        if nums[i] > nums[i + 1]:
            return i

    return len(nums) - 1


# Approach 2
# O(log2(n))

# Iterative Approach
def findPeakElementIterative(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        mid = l + (r - l) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


def findPeakElementRecursive(nums, l, r):
    if l == r:
        return l
    mid = l + (r - l) // 2
    if nums[mid] > nums[mid + 1]:
        return findPeakElementRecursive(nums, l, mid)
    return findPeakElementRecursive(nums, mid + 1, r)


arr = [1, 2, 1, 3, 5, 6, 4]
print("Linear:", findPeakElementLinear(arr))
print("Iterative:", findPeakElementIterative(arr))
print("Recursive:", findPeakElementRecursive(arr, 0, len(arr) - 1))
