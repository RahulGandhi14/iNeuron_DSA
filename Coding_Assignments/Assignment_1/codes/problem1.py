def findSqrt(num):
    left = 0
    right = num

    while left <= right:
        mid = left + (right-left)//2
        sqrt = mid*mid
        if(sqrt == num):
            return mid
        elif sqrt > num:
            right = mid - 1
        else:
            if((mid+1)*(mid+1)>num):
                return mid
            left = mid + 1

print(findSqrt(81))
    