def ternary_search(arr, left, right, target):
    while left <= right:
        mid1 = left + (right-left)//3
        mid2 = right - (right-left)//3

        if(arr[mid1]==target):
            return mid1
        elif arr[mid2]==target:
            return mid2
        elif arr[mid1] > target:
            return ternary_search(arr, left, mid1-1, target)
        elif arr[mid2] < target:
            return ternary_search(arr, mid2+1, right, target)
        else:
            return ternary_search(arr, mid1+1, mid2-1, target)
    return -1

arr = [1,2,3,4,5,6,7,8,9,10]
for each in arr:
    print(each, "->",ternary_search(arr, 0, len(arr)-1, each))
print(11,"->",ternary_search(arr, 0, len(arr)-1, 11))