## Time Complexity: O(n)
def merge_combine(arr, left, mid, right):
    ## length of first sub array
    n1 = mid - left + 1

    ## length of second sub array
    n2 = right - mid

    ## initialization of left and right sub array
    leftSubArr = [0] * n1
    rightSubArr = [0] * n2

    ## copy the elements from an array to sub arrays
    ## left sub array
    for i in range(n1):
        leftSubArr[i] = arr[left + i]
    ## right sub array
    for i in range(n2):
        rightSubArr[i] = arr[mid + 1 + i]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if leftSubArr[i] > rightSubArr[j]:
            arr[k] = rightSubArr[j]
            j += 1
        else:
            arr[k] = leftSubArr[i]
            i += 1
        k += 1

    ## Copy remaining elements for left sub array
    while i < n1:
        arr[k] = leftSubArr[i]
        i += 1
        k += 1

    ## Copy remaining elements for right sub array
    while j < n2:
        arr[k] = rightSubArr[j]
        j += 1
        k += 1


## Time Complexity: O(nlogn)
def merge_sort(arr, left, right):
    if left < right:
        ## Divide
        mid = left + (right - left) // 2
        ## Conquer
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        ## Combine
        merge_combine(arr, left, mid, right)

    return arr


arr = [1, 3, 7, 9, 12, 10, 8, 16, 18, 22, 27, 0]
print(merge_sort(arr, 0, len(arr) - 1))
