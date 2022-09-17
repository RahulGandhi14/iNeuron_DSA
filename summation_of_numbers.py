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


print(two_sum(arr, sum))