def isBadVersion(arr, idx):
    if(arr[idx]==0):
        return False
    else:
        return True

def findVersion(arr):
    left = 0
    right = len(arr)

    while left <= right:
        mid = left + (right - left)//2
        if(not isBadVersion(arr, mid)):
            if(mid + 1 <= right and mid + 1 < len(arr)):
                if(not isBadVersion(arr, mid+1)):
                    left = mid + 1
                else:
                    return mid
            else:
                return -1
        else:
            if(mid - 1 >= left and mid - 1 >= 0):
                if(isBadVersion(arr, mid-1)):
                    right = mid - 1
                else:
                    return mid - 1
            else:
                return -1
    return -1

print(findVersion([0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1]))
            

