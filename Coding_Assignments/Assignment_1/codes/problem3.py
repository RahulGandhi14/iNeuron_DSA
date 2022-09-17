def isPerfectSquare(self, num: int) -> bool:
    if(num==1 or num==0): return num
    
    left = 0
    right = num//2

    while left <= right:
        mid = left + (right-left)//2
        sqrt = mid*mid
        if(sqrt == num):
            return True
        elif sqrt > num:
            right = mid - 1
        else:
            left = mid + 1
    return False

print(isPerfectSquare(16))
print(isPerfectSquare(14))