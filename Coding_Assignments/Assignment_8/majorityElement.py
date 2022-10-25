# PROBLEM 4
def majorityElement(nums):
    hashMap = dict()
    majority = None
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        if hashMap[num] >= len(nums) / 2:
            majority = num
    return majority


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
