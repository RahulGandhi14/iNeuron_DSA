arr = [0,1,5,7,10,11,19,21,27,30]

def recursive_binary_search(arr, item, start, end):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return recursive_binary_search(arr, item, start, mid-1)
        else:
            return recursive_binary_search(arr, item, mid+1, end)
    return -1

def iterative_binary_search(arr, item, start, end):
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# print(recursive_binary_search(arr,27,0,len(arr)))
# print(iterative_binary_search(arr,27,0,len(arr)))


# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #
# ---------------------------- Practice Problems ----------------------------- #
# --------------------------------------------------------------------- #
# --------------------------------------------------------------------- #

# 1. Find indices of integers from the sorted array whose sum is equal to give target_sum.

# 1. Brute Force Approach: use two loops. O(n)
# 2. Use Single loop and Binary search for second index. O(nlogn)
# 3. Two Pointer Approach

arr = [10,20,30,40,90,120,220,500]
sum = 201

def two_sum(arr, sum):
    left = 0
    right = len(arr) -1
    while left < right:
        summation = arr[left] + arr[right]
        if summation == sum:
            return [left,right]
        elif summation < sum:
            left += 1
        else:
            right -= 1
    return [-1,-1]


# print(two_sum(arr, sum)) 


# 2. Find Maximum profit from the array of stock prices of 7 days
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solution/
arr = [7,1,5,3,6,4,4]

def maxProfit(prices):
    min = 0;
    profit = 0;
    for i in range(len(prices)):
        if(i==0):
            min = prices[i]
            continue
        if(min > prices[i]):
            min = prices[i]
        
        sum = prices[i] - min
        if(sum > profit):
            profit = sum
    return profit

# print("MAX: ", maxProfit(arr))





# 3. Find row idx and col idx of an element.
# https://leetcode.com/problems/search-a-2d-matrix/

# arr = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# arr = [[1,1]]
arr = [[1]]

def get_mid( col_len, mid):
    row_idx = (mid // col_len)
    col_idx = mid % col_len
    return [row_idx,col_idx]

def binary_search_2d(arr, item, left, right, row_len, col_len):
    while left <= right:
        mid = left + (right-left)//2
        mid_idx = get_mid(col_len, mid)

        if(mid_idx[0]>=row_len or mid_idx[1]>=col_len):
            return [-1,-1]

        element = arr[mid_idx[0]][mid_idx[1]]
        if(element == item):
            return mid_idx
        elif element > item:
            right = mid - 1
        else:
            left = mid + 1
    return [-1,-1]

# print("BINARY_2D", binary_search_2d(arr, 2, 0, (len(arr[0])*len(arr)), len(arr), len(arr[0])))


# 4. https://leetcode.com/problems/search-a-2d-matrix/

# arr = [3,2,4]
arr = [3,3]

def TwoSum(arr,target):
    hashTable = dict()
    for i in range(len(arr)):
        if(hashTable.keys().__contains__(arr[i])):
            return [hashTable[arr[i]], i]
        else:
            hashTable[target-arr[i]] = i

# print(TwoSum(arr,6))