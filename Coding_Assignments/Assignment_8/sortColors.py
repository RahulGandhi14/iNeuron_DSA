# https://leetcode.com/problems/sort-colors/

# We can also use counting sort.
# count number of 0s, 1s and 2s. And place the same as per the count.
# Time Complexity: O(2n)


# Time Complexity: O(n)
def sortColors(nums):
    second = len(nums) - 1
    zero = 0
    for idx in range(len(nums)):
        while nums[idx] == 2 and idx < second:
            nums[idx], nums[second] = nums[second], nums[idx]
            second -= 1
        while nums[idx] == 0 and idx > zero:
            nums[idx], nums[zero] = nums[zero], nums[idx]
            zero += 1

    return nums


print(sortColors([2, 0, 1]))
print(sortColors([2, 0, 2, 1, 1, 0]))
