def threeSumClosest(nums, target):
    nums.sort()
    closest = None
    for currIdx in range(len(nums) - 2):
        left = currIdx + 1
        right = len(nums) - 1
        while left < right:
            currentSum = nums[currIdx] + nums[left] + nums[right]
            if currentSum == target:
                return currentSum

            if closest is None or abs(currentSum - target) < abs(closest - target):
                closest = currentSum

            if currentSum < target:
                left += 1
            elif currentSum > target:
                right -= 1

    return closest


nums = [4, 0, 5, -5, 3, 3, 0, -4, -5]
print(threeSumClosest(nums, -2))
