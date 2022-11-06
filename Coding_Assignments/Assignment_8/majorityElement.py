import collections

# PROBLEM 4
def majorityElement(nums):
    hashMap = dict()
    majority = None
    for num in nums:
        hashMap[num] = hashMap.get(num, 0) + 1
        if hashMap[num] >= len(nums) / 2:
            majority = num
    return majority


def approach2(nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)


# Both above approaches uses extra O(n) space.

# Most Optimized is Boyer Moore Voting Alogirth


def boyerMoore(nums):
    target = None
    count = 0
    for num in nums:
        if count == 0:
            target = num

        count += 1 if target == num else -1

    return target


print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(approach2([2, 2, 1, 1, 1, 2, 2, 1, 1]))
print(boyerMoore([2, 2, 1, 1, 1, 2, 2, 1, 1]))
